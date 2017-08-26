from django.db import models

class Pupil(models.Model):
    name = models.CharField(verbose_name='Name', )
    surname = models.CharField(verbose_name='Surname')
    email = models.EmailField(verbose_name='Email')
    school = models.CharField(verbose_name='School')
    grade = models.CharField(verbose_name='Grade')