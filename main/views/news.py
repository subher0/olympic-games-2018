from django.http import HttpResponse
from django.template import loader
from ..models.news import News

def news_view(request):
    news = News.objects.getAllNews()
    context = {
        'news': news,
    }
    template = loader.get_template('main/news.html')
    return HttpResponse(template.render(context, request))
