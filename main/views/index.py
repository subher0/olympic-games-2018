from django.http import HttpResponse
from django.template import loader

from main.models import Project, Tagline, Partner
from main.models import News


def index_view(request):
    template = loader.get_template('main/index.html')
    projects = Project.objects.getSomeProjects(5)
    news = News.objects.getSomeNews(3)
    tagline = Tagline.objects.getRandomTagline()
    partners = Partner.objects.getAllPartners()
    context = {
        'upperProjects': projects[:3],
        'lowerProjects': projects[3:5],
        'news': news,
        'tagline': tagline,
        'partners': partners,
    }
    return HttpResponse(template.render(context, request))
