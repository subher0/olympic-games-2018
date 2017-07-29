from django.contrib import admin

from .models.article import Article
from .models.profile import Profile

admin.site.register(Article)
admin.site.register(Profile)
