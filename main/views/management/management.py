import uuid

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader, TemplateDoesNotExist

from main.forms.management_form import ManagementForm, LoginForm
from main.models import Chump
from main.models.management.manager import Manager
from main.models.projects.university_saturdays import Auditory, EventType, Subject, Event
from main.models.university import University


def management_view(request, form=None, errorMessage=None, success_message=None):
    manager = Manager.objects.filter(secret=request.COOKIES.get('secret')).first()
    if manager is None:
        return login_view(request)
    universities = manager.universities.all()

    auditories = Auditory.objects.all()
    eventTypes = EventType.objects.all()
    subjects = Subject.objects.all()

    context = {
        'form': form,
        'universities': universities,
        'auditories': auditories,
        'types': eventTypes,
        'subjects': subjects,
        'error_message': errorMessage,
        'success_message': success_message
    }

    if form is not None:
        context['university_id'] = int(form.data['university'])
        context['auditory_id'] = int(form.data['auditory'])
        context['type_id'] = int(form.data['type'])
        context['subject_id'] = int(form.data['subject'])

    try:
        template = loader.get_template('main/management/management.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))


def register_university_saturday(request):
    manager = Manager.objects.filter(secret=request.COOKIES.get('secret')).first()
    if manager is None:
        return login_view(request)

    error_message = ''
    success_message = None

    form = None
    if request.method == 'POST':
        form = ManagementForm(request.POST)
        if form.is_valid():
            try:
                university = University.objects.get(id=form.cleaned_data.get('university'))
                auditory = Auditory.objects.get(id=form.cleaned_data.get('auditory'))
                type = EventType.objects.get(id=form.cleaned_data.get('type'))
                subject = Subject.objects.get(id=form.cleaned_data.get('subject'))
                event = Event(date=form.cleaned_data.get('date'), title=form.cleaned_data.get('title'),
                              location=form.cleaned_data.get('location'), description=form.cleaned_data.get('description'),
                              maximumCapacity=form.cleaned_data.get('maximumCapacity'), currentlyRegistered=0)
                event.subject = subject
                event.university = university
                event.save()
                event.auditory.add(auditory)
                event.types.add(type)
                event.save()
                success_message = 'Вы успешно зарегистрировали субботу!'
            except Exception:
                error_message = 'Ошибка в полях формы, либо в базе данных. Если вы уверены, что ошибки в полях нет, напишите в поддержку сайта (смотрите подвал сайта)'
        else:
            error_message = 'Ошибки в полях формы'
    else:
        error_message = 'Неподдерживаемый тип запроса'

    if error_message == '':
        return redirect('/management?success_message=%s' % success_message)

    return management_view(request, form, error_message, success_message)


def login_view(request):
    error_message = ''
    success_message = None

    response = None
    form = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            manager = Manager.objects.filter(name=form.cleaned_data['login'], password=form.cleaned_data['password']).first()
            if manager is not None:
                manager.secret = str(uuid.uuid4())
                response = HttpResponse()
                response.set_cookie('secret', manager.secret)
                response.status_code = 302
                response['Location'] = '/management'
                manager.save()
                return response

    context = {
    }
    try:
        template = loader.get_template('main/management/login.html')
        response = HttpResponse(template.render(context, request))
    except TemplateDoesNotExist:
        raise Http404
    return response
