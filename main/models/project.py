from django.db import models
from django.utils.timezone import now
from .utils import make_filepath
from uuid import uuid4

class ProjectManager(models.Manager):
    def getAllProjects(self):
        try:
            result = self.order_by('date')
        except Exception:
            result = None
        return result

    def getSomeProjects(self, amount):
        try:
            result = self.order_by('date')[:amount]
        except Exception:
            result = None
        return result


class Project(models.Model):
    date = models.DateTimeField(verbose_name='publication date', default=now)
    title = models.TextField(verbose_name='project title')
    text = models.TextField(verbose_name='project text')
    description = models.TextField(verbose_name='project description', max_length=256, default='No description')
    icon = models.FileField(verbose_name='project icon', default='no_icon.svg', upload_to=make_filepath)
    objects = ProjectManager()

    def __str__(self):
        return self.title
