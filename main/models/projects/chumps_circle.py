from django.db import models
from django.utils.timezone import now
from main.models.utils import make_filepath


class ChumpManager(models.Manager):
    def getAllChumps(self):
        try:
            result = self.order_by('priority', 'id')
        except Exception:
            result = None
        return result

    def getSomeChumps(self, amount):
        try:
            result = self.order_by('priority', 'id')[:amount]
        except Exception:
            result = None
        return result


class Chump(models.Model):
    name = models.TextField(verbose_name='Name')
    priority = models.IntegerField(verbose_name='Priority (optional)', default=0)
    about_short = models.TextField(verbose_name='Very brief description', max_length=128, default='Good guy and all')
    about = models.TextField(verbose_name='About')
    specialty = models.TextField(verbose_name='Specialty')
    university = models.TextField(verbose_name='University', default='ДГУ')
    image = models.ImageField(verbose_name='news image', default='no_image.png', upload_to=make_filepath)
    objects = ChumpManager()

    def __str__(self):
        return self.name
