from django.db import models
from django.utils.timezone import now
from .utils import make_filepath

class PartnerManager(models.Manager):
    def getAllPartners(self):
        try:
            result = self.order_by('date')
        except Exception:
            result = None
        return result

    def getSomePartners(self, amount):
        try:
            result = self[:amount]
        except Exception:
            result = None
        return result


class Partner(models.Model):
    date = models.DateTimeField(verbose_name='publication date', default=now)
    text = models.TextField(verbose_name='Text under partner')
    link = models.TextField(verbose_name='Link to partner', max_length=256, default='No description')
    icon = models.FileField(verbose_name='Partner image', default='no_image.png', upload_to=make_filepath)
    objects = PartnerManager()

    def __str__(self):
        return self.text
