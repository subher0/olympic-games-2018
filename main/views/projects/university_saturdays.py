import os
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader, TemplateDoesNotExist

from main.forms.event_reg_form import EventSignupForm, EventSearchForm
from main.models import Chump, Pupil
from main.models.projects.university_saturdays import Event, EventType, Auditory, Subject
from main.models.university import University


def university_saturdays_view(request):
    events = Event.objects.getAllEvents()
    types = EventType.objects.all()
    auditories = Auditory.objects.all()
    subjects = Subject.objects.all()
    univesities = University.objects.getAllUniversities()
    success_message = ''
    try:
        success_message = request.GET['success_message']
    except Exception:
        pass

    context = {
        'events': events,
        'types': types,
        'auditories': auditories,
        'subjects': subjects,
        'universities': univesities,
        'success_message': success_message
    }
    try:
        template = loader.get_template('main/projects/university_saturdays.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))


def send_email_to_university_and_save(event):
    message = ''
    people = Pupil.objects.getByEvent(event)
    for person in people:
        message += 'Имя: ' + person.name + '\n' + 'Email: ' + person.email + '\n' + \
                   'Имя: ' + person.phone + '\n' + \
                   'Школа: ' + person.school + ', класс: ' + str(person.grade) + '\n' + '----------------------------\n'
    send_mail(subject='Зарегистрировавшиеся на ' + event.title,
              message=message, from_email=os.environ.get('OLIMP_EMAIL_HOST_USER'),
              recipient_list=[event.university.email])
    event.isClosed = True
    event.save()


def signup_for_event(request):
    form = EventSignupForm()
    events = Event.objects.getAllEvents()
    error_message = ''
    success_message = 'Вы успешно зарегестрировались на событие!'
    if request.method == 'POST':
        form = EventSignupForm(request.POST)
        if form.is_valid():
            event = Event.objects.getById(form.cleaned_data['eventId'])
            if event.currentlyRegistered > event.maximumCapacity or event.isClosed:
                error_message = 'К сожалению, регистрация уже закрыта.'
            elif event.currentlyRegistered == event.maximumCapacity:
                # Send message when full
                send_email_to_university_and_save(event)
            else:
                event.currentlyRegistered += 1
                event.university.rating += 1
                event.university.save()
                Pupil.objects.createPupil(form.cleaned_data['nameField'], form.cleaned_data['phoneField'],
                                          form.cleaned_data['emailField'], form.cleaned_data['schoolField'],
                                          form.cleaned_data['gradeField'], event)
                event.save()
        else:
            error_message = 'Ошибки в полях формы'
    else:
        error_message = 'Неподдерживаемый тип запроса'

    if error_message == '':
        return redirect('/projects/university_saturdays?success_message=%s' % success_message)

    types = EventType.objects.all()
    auditories = Auditory.objects.all()
    subjects = Subject.objects.all()
    univesities = University.objects.getAllUniversities()

    context = {
        'error_message': error_message,
        'form': form,
        'events': events,
        'types': types,
        'auditories': auditories,
        'subjects': subjects,
        'universities': univesities,
    }

    try:
        template = loader.get_template('main/projects/university_saturdays.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))


def eventSearch(request):
    form = None
    error_message = ''
    events = None
    if request.method == 'GET':
        form = EventSearchForm(request.GET)
        if form.is_valid():
            university = form.cleaned_data['university']
            subject = form.cleaned_data['subject']
            eventType = form.cleaned_data['eventType']
            auditory = form.cleaned_data['auditory']
            events = Event.objects.all()

            if university != 0:
                events = events.filter(university__id=university)
            elif subject != 0:
                events = events.filter(subject__id=subject)
            elif eventType != 0:
                events = events.filter(type__id=eventType)
            elif auditory != 0:
                events = events.filter(auditory__id=auditory)

            events = events.order_by('date')
        else:
            error_message = 'Ошибки в полях формы'
    else:
        error_message = 'Неподдерживаемый тип запроса'

    types = EventType.objects.all()
    auditories = Auditory.objects.all()
    subjects = Subject.objects.all()
    universities = University.objects.getAllUniversities()

    context = {
        'error_message': error_message,
        'form': form,
        'events': events,
        'types': types,
        'auditories': auditories,
        'subjects': subjects,
        'universities': universities,
    }

    try:
        template = loader.get_template('main/projects/university_saturdays.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))
