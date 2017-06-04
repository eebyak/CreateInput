# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LinguisticRule(models.Model):
    name = models.CharField(max_length=200,default='')
    description = models.TextField('Missing Description')
    rule = models.CharField(max_length=200,default='')

    def __str__(self):
       return self.name


class LinguisticQuestion(models.Model):
    name = models.CharField(max_length=200,default='')
    question = models.CharField(max_length=200,default='')

    def __str__(self):
       return self.name


