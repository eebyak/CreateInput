# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Linguistics', '0002_auto_20170605_0529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linguisticrule',
            name='rule',
        ),
        migrations.AddField(
            model_name='linguisticrule',
            name='CVC',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='linguisticrule',
            name='gr',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='linguisticrule',
            name='ph',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='linguisticrule',
            name='word',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
