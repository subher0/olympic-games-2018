from django.db import models
from main.models.utils import make_filepath


class FamousOneManager(models.Manager):
    def getAllFamousOnes(self):
        try:
            result = self.order_by('id').reverse()
        except Exception:
            result = None
        return result

    def getSomeFamousOnes(self, amount):
        try:
            result = self.order_by('id').reverse()[:amount]
        except Exception:
            result = None
        return result


class FamousOne(models.Model):
    name = models.TextField(verbose_name='Name')
    about = models.TextField(verbose_name='About')
    specialty = models.TextField(verbose_name='Specialty')
    image = models.ImageField(verbose_name='news image', default='no_image.png', upload_to=make_filepath)
    objects = FamousOneManager()

    def __str__(self):
        return self.name
