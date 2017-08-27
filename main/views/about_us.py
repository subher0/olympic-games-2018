from django.http import HttpResponse
from django.template import loader


def about_view(request):
    template = loader.get_template('main/about_us.html')
    return HttpResponse(template.render({}, request))
