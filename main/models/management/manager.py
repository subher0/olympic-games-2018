from django.db import models

from main.models.university import University


class Manager(models.Model):
    name = models.CharField(verbose_name='Login', max_length=50)
    password = models.CharField(verbose_name='Password', max_length=50)
    secret = models.CharField(verbose_name='Secret', default='Тут ниче не пиши, оно само генерится', max_length=128)
    universities = models.ManyToManyField(University, verbose_name='Universities that he manages')
    rating = models.IntegerField(verbose_name='Rating, так, для хаха', default=0)

    def __str__(self):
        return self.name