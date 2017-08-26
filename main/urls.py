from django.conf.urls import url

from main.views.projects import chumps_circle
from .views import contacts
from .views import index
from .views import news
from .views import olympics

urlpatterns = [
    url(r'^$', index.index_view, name='index'),
    url(r'^news$', news.news_view, name='news'),
    url(r'^olympics$', olympics.olympics_view, name='olympics'),
    url(r'^contacts$', contacts.contacts_view, name='contacts'),
    url(r'^projects/chumps_circle$', chumps_circle.chump_circle_view, name='chumps_circle'),
]
