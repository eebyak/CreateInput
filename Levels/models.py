# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.db import models

# Create your models here.

class Level(models.Model):
    type = models.CharField(max_length=200,default='',null=True)
    name = models.CharField(max_length=200, default='', null=True)
    level = models.IntegerField(default='', null=True)
    list = models.TextField(default='', null=True)

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def __str__(self):
        return "%s is a %s" % (self.name, self.level)


class LetterLevels(Level):
    def __init__(self, type):
        super(Level, self).__init__()
        self.type = type

    def check_level(self,letter):
        target = self.list.split()
        print >> sys.stderr, target
        if letter in target:
            return True

        return False


class WordLevels(Level):
    # def __init__(self):
    #     Level.__init__(self)
    #
    def __init__(self, type):
        super(Level, self).__init__()
        self.type = type

    def check_level(self,word):
        # we can use Wortschatz Niveau hier later
        return True


class CVCLevels(Level):
    def __init__(self, type):
        super(Level, self).__init__()
        self.type = type

    def check_level(self,pattern):
        if pattern in self.list.split():
            return True
        return False



