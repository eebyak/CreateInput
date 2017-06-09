# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import sys

from django.contrib import messages

from Database.constants import high_freq_L2, high_freq_L1
from django.db import models
from Levels.models import Level


# Create your models here.




class Dictionary (models.Model):
    language_id = models.IntegerField(default=1)
    language = models.CharField(max_length=200,default="DE")

    def __str__(self):
        return self.language

    def select_entries_by_letter(self,pre_entries, pattern):
        letters = pattern.split()
        entries = list()
        for entry in pre_entries:
            spelling = entry.gr.split()
            for letter in letters:
                # if l in spelling:
                length = len(spelling)
                # print >> sys.stderr, letter, length
                # if (length == 2):
                #     if ((letter == spelling[0]) or (letter == spelling[1])):
                #         entries.append(entry)
                if (length > 1):
                    if ((letter == spelling[0]) or (letter == spelling[1]) ):
                        entries.append(entry)

        return entries

    def find_Matches(self,key,pattern):
        entries = ()
        message=""
        if (key == "CVC"):
            entries = Entry.objects.filter(CVC=pattern, HFW=False)
        if (key == "letter"):
            message="If I were to give you words that only have this letter, then I would have problems! " \
                    " Instead, I will give you all words that contain this letter in the first two positions only." \
                    " Extrapolate from there. Anyhow, you will use this jointly with other patterns in Linguistic Rules secion, " \
                    "so this listing is just a debugging aid."
            pre_entries = Entry.objects.filter(HFW=False)
            entries = self.select_entries_by_letter(pre_entries, pattern)
        # if (key == "letters"): entries = Entry.objects.filter()
        else:
            message="this key does not exist in the code yet. We have CVC, letter. Change in find_Matches in Database/models.py"

        return entries, message

class Entry(models.Model):
    dictionary = models.ForeignKey(Dictionary,default='',null=True)
    word = models.CharField(max_length=200,default='',null=True)
    CVC = models.CharField(max_length=200,default='',null=True)
    gr = models.CharField(max_length=200,default='',null=True)
    ph = models.CharField(max_length=200,default='',null=True)
    HFW = models.BooleanField(default=False)

    # def __init__(self,dictionary):
    #     super.__init__()
    #     self.dictionary = dictionary

    def __str__(self):
        return self.word

    def __unicode__(self):
        return self.word

    def get_entry(self):
        return "{0} with pronunciation {1}".format(self.word, self.ph)


    def get_HFW(self):
        word = self.word.lower()
        if (word in high_freq_L1) or (word in high_freq_L2):
            self.HFW = True
        else:
            self.HFW = False




    # def get_json(self):
        # d = self.__dict__
        # jsonarray = json.dumps(d)
        # return jsonarray


def find_letter_match(pre_entries, letters, index):
    entries = list()
    #print sys.stderr, letters
    for e in pre_entries:
        spelling = e.gr.split()
        if (spelling[index] in letters):
            entries.append(e)

    return entries

def get_entries_that_match(instance):
    word = instance.word
    ph = instance.ph
    gr = instance.gr
    CVC = instance.CVC

    # inits
    message = ""
    spellint = list()
    entries = list()
    pre_entries = list()

    # debug
    #print >> sys.stderr, word, ph, gr, CVC

    # FIRST CHECK sublist of words to be used:
    if (word != '*'):
        if (word == "HFW"):
            pre_entries = Entry.objects.filter(HFW=True)
        else:
            pre_entries = Entry.objects.filter(HFW=False)
            message = "we dont have levels of word lists yet, so i will just get all for now."
    else:
        pre_entries = Entry.objects.filter(HFW=False)

    #print >> sys.stderr, "After word match: ", len(pre_entries)

    # check for dont care otherwiese, pick descired CVC structures
    if (CVC != '*'):
        # entries = entries.filter(CVC=CVC)
        pre_entries = filter(lambda x: x.CVC == CVC, pre_entries)

    if (ph != '*'):
        message = "I have not implemented this yet in Database/models.py get_entries_that_match"

    if (gr != '*'):
        spelling = gr.split()
        #print >> sys.stderr, spelling, gr
        for idx, symbol in enumerate(spelling):
            #print >> sys.stderr, type(symbol)
            #print >> sys.stderr, symbol
            if (symbol != '*'):
                symbol = int(symbol)
                #print >> sys.stderr, type(symbol)
                try:
                    level = Level.objects.get(pk=symbol)
                    #print >> sys.stderr, level.type, level.list
                    letters = level.list.split()
                    #print >> sys.stderr, letters
                    pre_entries = find_letter_match(pre_entries, letters, idx)
                except Level.DoesNotExist:
                    message = message + "  You made a mistake with the ID number %d in grapheme description" % symbol

    #entries = [item for sublist in pre_entries for item in sublist]
    entries = pre_entries

    return(entries,message)
