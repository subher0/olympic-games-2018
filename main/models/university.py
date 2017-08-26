from django.db import models


class UniversityManager(models.Manager):
    def getAllUniversities(self):
        try:
            result = self.order_by('name').reverse()
        except Exception:
            result = None
        return result

    def getSomeUniversities(self, amount):
        try:
            result = self.order_by('name').reverse()[:amount]
        except Exception:
            result = None
        return result


class University(models.Model):
    name = models.TextField(verbose_name='Name')
    about = models.TextField(verbose_name='About')
    rating = models.IntegerField(verbose_name='rating', default=0)
    email = models.EmailField(verbose_name='Email')
    objects = UniversityManager()

    def __str__(self):
        return self.name
