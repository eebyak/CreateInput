# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0004_auto_20170605_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gametype',
            name='description',
            field=models.TextField(default='Missing Description', null=True),
        ),
        migrations.AlterField(
            model_name='gametype',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
