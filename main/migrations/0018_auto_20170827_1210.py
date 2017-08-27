# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_famousone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('title', models.TextField(verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('maximum_capacity', models.IntegerField(verbose_name='Maximum capacity')),
                ('currentlyRegistered', models.IntegerField(editable=False, verbose_name='Currently registered')),
                ('image', models.ImageField(default='no_image.png', upload_to=main.models.utils.make_filepath, verbose_name='news image')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('rating', models.IntegerField(default=0, verbose_name='rating')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.RemoveField(
            model_name='famousone',
            name='about_short',
        ),
        migrations.RemoveField(
            model_name='famousone',
            name='achievements',
        ),
        migrations.AddField(
            model_name='event',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.University', verbose_name='University'),
        ),
    ]
