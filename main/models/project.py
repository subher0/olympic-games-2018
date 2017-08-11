from django.db import models
from django.utils.timezone import now
from .utils import make_filepath
from uuid import uuid4

class ProjectManager(models.Manager):
    def getAllProjects(self):
        try:
            result = self.order_by('date').reverse()
        except Exception:
            result = None
        return result

class Project(models.Model):
    date = models.DateTimeField(verbose_name='publication date', default=now)
    title = models.TextField(verbose_name='project title')
    text = models.TextField(verbose_name='project text')
    description = models.TextField(verbose_name='project description', max_length=256, default='No description')
    image = models.ImageField(verbose_name='project image', default='no_image.jpg', upload_to=make_filepath)
    objects = ProjectManager()

    def __str__(self):
        return self.title
