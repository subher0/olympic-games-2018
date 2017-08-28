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
    form = EventSearchForm()
    error_message = ''
    success_message = 'Вы успешно зарегестрировались на событие!'
    if request.method == 'GET':
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
    events = Event.objects.getAllEvents()

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