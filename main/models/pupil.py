from django.db import models
from django.db.models import Manager

from main.models.projects.university_saturdays import Event


class PupilManager(Manager):
    def createPupil(self, name, phone, email, school, grade, event):
        pupil = Pupil(name=name, phone=phone, email=email, school=school, grade=grade, event=event)
        pupil.save()


class Pupil(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone', default='Nan', max_length=20)
    school = models.CharField(verbose_name='School', max_length=255)
    grade = models.IntegerField(verbose_name='Grade', default=0)
    event = models.ForeignKey(Event, verbose_name='Event', default=None, null=True)

    objects = PupilManager()

    def __str__(self):
        return self.name + '|' + self.email