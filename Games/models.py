# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


import json

# Create your models here.


class GameType(models.Model):
    name = models.CharField(max_length=200,default='NoName',null=True)
    description = models.TextField(default='Missing Description',null=True)
    # linguistic_rule_input = models.ForeignKey('Linguistics.LinguisticRule', related_name='input',null=True)
    # linguistic_rule_output = models.ForeignKey('Linguistics.LinguisticRule', related_name='output', null=True)
    # linguistic_rule_question = models.ForeignKey('Linguistics.LinguisticQuestion', null=True)

    def __str__(self):
       return self.name


class Game(models.Model):
    name = models.CharField(max_length=200,default='')
    type = models.ForeignKey(GameType)

    def __str__(self):
       return self.name

    def get_plain(self):
        return self