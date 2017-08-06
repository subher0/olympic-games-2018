from django.http import HttpResponse
from django.template import loader


def contacts_view(request):
    template = loader.get_template('main/contacts.html')
    return HttpResponse(template.render({}, request))
