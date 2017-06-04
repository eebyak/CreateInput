# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models


# Create your models here.

class Dictionary (models.Model):
    language_id = models.IntegerField(default=1)
    language = models.CharField(max_length=200,default="DE")

    def __str__(self):
       return self.language



class Entry(models.Model):
    dictionary = models.ForeignKey(Dictionary)
    word = models.CharField(max_length=200,default='')
    CVC = models.CharField(max_length=200,default='')
    gr = models.CharField(max_length=200,default='')
    ph = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.word

    def get_entry(self):
        return "{0} with pronunciation {1}".format(self.word, self.ph)

    # def get_json(self):
        # d = self.__dict__
        # jsonarray = json.dumps(d)
        # return jsonarray
