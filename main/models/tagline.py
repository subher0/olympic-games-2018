from django.db import models
from django.utils.timezone import now
from .utils import make_filepath

class TaglineManager(models.Manager):
    def getAllTaglines(self):
        try:
            result = self
        except Exception:
            result = None
        return result

    def getRandomTagline(self, amount):
        try:
            result = self.order_by('date')[:amount]
        except Exception:
            result = None
        return result


class Tagline(models.Model):
    title = models.TextField(verbose_name='Tagline title')
    text = models.TextField(verbose_name='Tagline text')

    def __str__(self):
        return self.title
