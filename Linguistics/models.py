# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LinguisticRule(models.Model):
    name = models.CharField(max_length=200,default='', null=True)
    description = models.TextField(default='Missing Description')
    rule = models.CharField(max_length=200,default='', null=True)

    def __str__(self):
       return self.name


class LinguisticQuestion(models.Model):
    name = models.CharField(max_length=200,default='', null=True)
    question = models.CharField(max_length=200,default='', null=True)

    def __str__(self):
       return self.name


