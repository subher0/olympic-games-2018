# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170804_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 10, 49, 51, 273857, tzinfo=utc), verbose_name='publication date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 10, 49, 51, 275753, tzinfo=utc), verbose_name='publication date'),
        ),
    ]
