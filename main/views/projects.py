from django.http import HttpResponse
from django.template import loader

def projects_view(request):
    template = loader.get_template('main/projects.html')
    return HttpResponse(template.render({}, request))
