from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from .utils import make_filepath


class ArticleManager(models.Manager):
    def getAllArticles(self):
        try:
            result = self.order_by('date').reverse()
        except Exception:
            result = None
        return result


class Article(models.Model):
    date = models.DateTimeField(verbose_name='publication date', default=now)
    title = models.TextField(verbose_name='article title')
    short_text = models.CharField(verbose_name='article short text', max_length=512, default='No description')
    text = models.TextField(verbose_name='article text')
    image = models.ImageField(verbose_name='article image', default='no_image.jpg', upload_to=make_filepath)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ArticleManager()

    def __str__(self):
        return self.title