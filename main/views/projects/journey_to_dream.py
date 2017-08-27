from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader, TemplateDoesNotExist

from main.models import Chump


def journey_to_dream_view(request):
    context = {}
    try:
        template = loader.get_template('main/projects/journey_to_dream.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))
