# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wordout', '0002_auto_20170606_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationtable',
            name='linguistic_rule_question',
            field=models.CharField(default='Question', max_length=200),
        ),
    ]