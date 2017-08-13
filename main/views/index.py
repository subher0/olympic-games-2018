from django.http import HttpResponse
from django.template import loader
from ..models.project import Project
from ..models.news import News


def index_view(request):
    template = loader.get_template('main/index.html')
    projects = Project.objects.getSomeProjects(4)
    news = News.objects.getSomeNews(1)
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))
