# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Linguistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linguisticquestion',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='linguisticquestion',
            name='question',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='linguisticrule',
            name='description',
            field=models.TextField(default='Missing Description'),
        ),
        migrations.AlterField(
            model_name='linguisticrule',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='linguisticrule',
            name='rule',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
