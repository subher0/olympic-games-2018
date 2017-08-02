from django.http import HttpResponse
from django.template import loader

def index_view(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))
