from django.http import HttpResponse
from django.template import loader

def olympics_view(request):
    template = loader.get_template('main/olympics.html')
    return HttpResponse(template.render({}, request))
