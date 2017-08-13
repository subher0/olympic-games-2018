from django.db import models
from django.utils.timezone import now
from .utils import make_filepath
from uuid import uuid4

class NewsManager(models.Manager):
    def getAllNews(self):
        try:
            result = self.order_by('date').reverse()
        except Exception:
            result = None
        return result

    def getSomeNews(self, amount):
        try:
            result = self.order_by('date').reverse()[:amount]
        except Exception:
            result = None
        return result


class News(models.Model):
    date = models.DateTimeField(verbose_name='publication date', default=now)
    title = models.TextField(verbose_name='news title')
    text = models.TextField(verbose_name='news text')
    short_text = models.TextField(verbose_name='news short text', max_length=512, default='No description')
    image = models.ImageField(verbose_name='news image', default='no_image.jpg', upload_to=make_filepath)
    objects = NewsManager()

    def __str__(self):
        return self.title
