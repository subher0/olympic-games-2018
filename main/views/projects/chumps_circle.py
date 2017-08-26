from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader, TemplateDoesNotExist

from main.models import Chump


def chump_circle_view(request):
    chumps = Chump.objects.getAllChumps()
    context = {
        'chumps': chumps
    }

    try:
        template = loader.get_template('main/projects/chumps_circle.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))
