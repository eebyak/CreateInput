# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0003_auto_20170604_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gametype',
            name='linguistic_rule_input',
        ),
        migrations.RemoveField(
            model_name='gametype',
            name='linguistic_rule_output',
        ),
        migrations.RemoveField(
            model_name='gametype',
            name='linguistic_rule_question',
        ),
    ]
