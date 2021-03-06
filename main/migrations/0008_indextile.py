# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import main.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170811_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('title', models.CharField(max_length=64, verbose_name='Tile title')),
                ('icon', models.ImageField(default='no_icon.jpg', upload_to=main.models.utils.make_filepath, verbose_name='Tile icon')),
                ('iconOnHover', models.ImageField(default='no_icon-reversed.jpg', upload_to=main.models.utils.make_filepath, verbose_name='Icon on hover')),
                ('link', models.CharField(max_length=1024, verbose_name='Link to follow on click')),
            ],
        ),
    ]
