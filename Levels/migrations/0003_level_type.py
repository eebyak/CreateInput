# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Levels', '0002_auto_20170607_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='type',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]