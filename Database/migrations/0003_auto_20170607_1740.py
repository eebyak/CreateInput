# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0002_auto_20170604_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='dictionary',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Database.Dictionary'),
        ),
    ]
