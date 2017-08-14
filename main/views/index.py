from django.http import HttpResponse
from django.template import loader

from main.models import IndexTile
from main.models import Project
from main.models import News


def index_view(request):
    template = loader.get_template('main/index.html')
    projects = Project.objects.getSomeProjects(4)
    news = News.objects.getSomeNews(1)
    tiles = IndexTile.objects.getAllTiles()
    topTiles = tiles[:2]
    restTiles = tiles[2:]
    context = {
        'projects': projects,
        'news': news[0],
        'topTiles': topTiles,
        'tiles': restTiles,
    }
    return HttpResponse(template.render(context, request))
