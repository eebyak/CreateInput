# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Linguistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(verbose_name='Missing Description')),
                ('linguistic_rule_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input', to='Linguistics.LinguisticRule')),
                ('linguistic_rule_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='Linguistics.LinguisticRule')),
                ('linguistic_rule_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Linguistics.LinguisticQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Games.GameType'),
        ),
    ]
