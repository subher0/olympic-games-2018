from django.http import HttpResponse
from django.template import loader

from main.models import Project
from main.models import News


def index_view(request):
    template = loader.get_template('main/index.html')
    projects = Project.objects.getSomeProjects(5)
    news = News.objects.getSomeNews(3)
    context = {
        'upperProjects': projects[:3],
        'lowerProjects': projects[3:5],
        'news': news,
    }
    return HttpResponse(template.render(context, request))
