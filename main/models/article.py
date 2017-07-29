from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    date = models.DateTimeField('publication date')
    title = models.TextField(verbose_name='article title')
    text = models.TextField(verbose_name='article text')
    author = models.ForeignKey(User)