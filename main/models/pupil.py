from django.db import models
from django.db.models import Manager

from main.models.projects.university_saturdays import Event


class PupilManager(Manager):
    def createPupil(self, name, phone, email, school, grade, event):
        pupil = Pupil(name=name, phone=phone, email=email, school=school, grade=grade, event=event)
        pupil.save()

    def getByEvent(self, event):
        return self.filter(event=event).order_by('name')


class Pupil(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    email = models.CharField(verbose_name='Email', max_length=255)
    phone = models.CharField(verbose_name='Phone', default='Nan', max_length=255)
    school = models.CharField(verbose_name='School', max_length=255)
    grade = models.CharField(verbose_name='Grade', default='N/A', max_length=255)
    event = models.ForeignKey(Event, verbose_name='Event', default=None, null=True, on_delete=models.CASCADE)

    objects = PupilManager()

    def __str__(self):
        return self.name + '|' + self.email