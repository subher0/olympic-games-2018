from django.db import models

class Pupil(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    surname = models.CharField(verbose_name='Surname', max_length=255)
    email = models.EmailField(verbose_name='Email')
    school = models.CharField(verbose_name='School', max_length=255)
    grade = models.ImageField(verbose_name='Grade')