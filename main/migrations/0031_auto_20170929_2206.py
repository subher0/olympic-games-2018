# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20170906_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='currentlyRegistered',
            field=models.IntegerField(default=0, verbose_name="Currently registered (DON'T TOUCH THAT!!!, НЕ ТРОГАТЬ!!!)"),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='grade',
            field=models.CharField(default='Стерся при переводе с цифры на текст в базе данных', max_length=255, verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='phone',
            field=models.CharField(default='Nan', max_length=255, verbose_name='Phone'),
        ),
    ]
