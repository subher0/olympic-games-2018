from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

def handler404(request):
    template = loader.get_template('main/errors/../templates/main/404.html')
    return HttpResponseNotFound(template.render({}, request))