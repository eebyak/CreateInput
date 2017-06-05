# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Linguistics.models import LinguisticRule, LinguisticQuestion
from Games.models import Game, GameType

# Create your models here.



class AssociationTable(models.Model):
    name = models.CharField(max_length=200,default='Association')
    gameType = models.ForeignKey('Games.GameType')
    linguistic_rule_input = models.ForeignKey('Linguistics.LinguisticRule', related_name='input',null=True)
    linguistic_rule_output = models.ForeignKey('Linguistics.LinguisticRule', related_name='output', null=True)
    linguistic_rule_question = models.ForeignKey('Linguistics.LinguisticQuestion', null=True)

    def __str__(self):
       return self.name