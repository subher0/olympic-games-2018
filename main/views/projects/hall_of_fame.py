from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader, TemplateDoesNotExist

from main.models import Chump, FamousOne


def hall_of_fame_view(request):
    famousOnes = FamousOne.objects.getAllFamousOnes()
    context = {
        'famousOnes': famousOnes
    }
    try:
        template = loader.get_template('main/projects/hall_of_fame.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))
