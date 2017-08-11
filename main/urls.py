from django.conf.urls import include, url

from .views import index
from .views import olympics
from .views import news
from .views import projects
from .views import contacts
from .views import project

urlpatterns = [
    url(r'^$', index.index_view, name='index'),
    url(r'^news$', news.news_view, name='news'),
    url(r'^projects$', projects.projects_view, name='projects'),
    url(r'^olympics$', olympics.olympics_view, name='olympics'),
    url(r'^contacts$', contacts.contacts_view, name='contacts'),
    url(r'^projects/(?P<projectId>\d+)$', project.index_view, name='project'),
]
