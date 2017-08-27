from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader, TemplateDoesNotExist

from main.models import Chump


def university_saturdays_view(request):
    context = {}
    try:
        template = loader.get_template('main/projects/university_saturdays.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))
