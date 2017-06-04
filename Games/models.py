# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Linguistics.models import LinguisticQuestion, LinguisticRule


import json

# Create your models here.


class GameType(models.Model):
    name = models.CharField(max_length=200,default='')
    description = models.TextField('Missing Description')
    linguistic_rule_input = models.ForeignKey('Linguistics.LinguisticRule', related_name='input')
    linguistic_rule_output = models.ForeignKey('Linguistics.LinguisticRule', related_name='output')
    linguistic_rule_question = models.ForeignKey('Linguistics.LinguisticQuestion')

    def __str__(self):
       return self.name


class Game(models.Model):
    name = models.CharField(max_length=200,default='')
    type = models.ForeignKey(GameType)

    def __str__(self):
       return self.name

