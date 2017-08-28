from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader, TemplateDoesNotExist

from main.forms.event_reg_form import EventSignupForm
from main.models import Chump, Pupil
from main.models.projects.university_saturdays import Event, EventType, Auditory, Subject
from main.models.university import University


def university_saturdays_view(request):
    events = Event.objects.getAllEvents()
    types = EventType.objects.all()
    auditories = Auditory.objects.all()
    subjects = Subject.objects.all()
    univesities = University.objects.getAllUniversities()
    context = {
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


def signup_for_event(request):
    form = EventSignupForm()
    events = Event.objects.getAllEvents()
    types = EventType.objects.all()
    auditories = Auditory.objects.all()
    subjects = Subject.objects.all()
    univesities = University.objects.getAllUniversities()
    error_message = ''
    if request.method == 'POST':
        form = EventSignupForm(request.POST)
        if form.is_valid():
            event = Event.objects.getById(form.cleaned_data['eventId'])
            if event.currentlyRegistered > event.maximumCapacity:
                return redirect('/')
            event.currentlyRegistered += 1
            event.university.rating += 1
            event.save()
            Pupil.objects.createPupil(form.cleaned_data['nameField'], form.cleaned_data['phoneField'],
                                      form.cleaned_data['emailField'], form.cleaned_data['schoolField'],
                                      form.cleaned_data['gradeField'], event)
            return redirect('/')

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
