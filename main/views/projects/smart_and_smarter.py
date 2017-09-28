from django.http import HttpResponse
from django.template import loader


def smart_view(request):
    template = loader.get_template('main/projects/smart_and_smarter.html')
    return HttpResponse(template.render({}, request))
