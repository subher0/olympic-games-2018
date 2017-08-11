from django.contrib import admin

from .models.article import Article
from .models.profile import Profile
from .models.news import News
from .models.project import Project

admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(News)
admin.site.register(Project)
