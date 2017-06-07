# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_auto_20170607_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='CVC',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='dictionary',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Database.Dictionary'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='gr',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ph',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='word',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
