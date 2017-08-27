from django.db import models
from django.utils.timezone import now

from main.models.university import University
from main.models.utils import make_filepath


class EventManager(models.Manager):
    def getAllEvents(self):
        try:
            result = self.order_by('id').reverse()
        except Exception:
            result = None
        return result

    def getSomeEvents(self, amount):
        try:
            result = self.order_by('id').reverse()[:amount]
        except Exception:
            result = None
        return result


class Event(models.Model):
    date = models.DateTimeField(verbose_name='Date', default=now)
    title = models.TextField(verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    maximum_capacity = models.IntegerField(verbose_name='Maximum capacity')
    currentlyRegistered = models.IntegerField(verbose_name='Currently registered', editable=False, default=False)
    university = models.ForeignKey(University, verbose_name='University')
    image = models.ImageField(verbose_name='news image', default='no_image.png', upload_to=make_filepath)
    objects = EventManager()

    def __str__(self):
        return self.title
