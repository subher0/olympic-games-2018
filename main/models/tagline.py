from django.db import models
import random

class TaglineManager(models.Manager):
    def getAllTaglines(self):
        try:
            result = self
        except Exception:
            result = None
        return result

    def getRandomTagline(self):
        try:
            result = random.choice(self.all())
        except Exception:
            result = None
        return result


class Tagline(models.Model):
    title = models.TextField(verbose_name='Tagline title')
    text = models.TextField(verbose_name='Tagline text')
    objects = TaglineManager()

    def __str__(self):
        return self.title
