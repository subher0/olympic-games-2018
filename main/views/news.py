from django.http import HttpResponse
from django.template import loader

def news_view(request):
    template = loader.get_template('main/news.html')
    return HttpResponse(template.render({}, request))
