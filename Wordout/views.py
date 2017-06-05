# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from Games.models import Game, GameType
from Linguistics.models import LinguisticRule, LinguisticQuestion
from Wordout.models import AssociationTable

from Wordout.forms import associateForm, rulesForm
from Linguistics.forms import linguisticsRForm,linguisticsQForm
from Database.forms import entryForm

# Create your views here.

def index(request):
    return render(request, 'Wordout/index.html')


def wordout_associate(request):
    gametypes = GameType.objects.all()
    return render(request, 'Wordout/wordout_associate.html', {'gametypes': gametypes} )


def wordout_list(request):
    return render(request, 'Wordout/wordout_list.html')


def wordout_print(request):
    return render(request, 'Wordout/wordout_print.html')

def wordout_add_distractor(request, rpk, gpk):
    print >> sys.stderr, rpk, gpk
    gametype = GameType.objects.get(pk=gpk)
    rule = LinguisticRule.objects.get(pk=rpk)
    rform = rulesForm()
    lform = linguisticsRForm(instance=rule)
    wform = entryForm()
    entries = []
    num_entries = entries.__len__()
    return render(request, 'Wordout/wordout_add_distractor.html',
                  {'gametype': gametype, 'rule': rule,
                   'rform': rform, 'lform': lform,
                   'entries': entries, 'wform': wform,'num_entries': num_entries
                   })

def wordout_add(request,pk):
    gametype = GameType.objects.get(pk=pk)
    if request.method == 'POST':
        rule = request.POST.get('rules')
        return redirect('wordout_add_distractor', rpk=rule, gpk=pk)

    games = Game.objects.filter(type=gametype)
    associations = AssociationTable.objects.filter(gameType=gametype)
    chosenRules = []
    for association in associations.iterator():
        chosenRules.append(association.linguistic_rule_input)

    allRules = LinguisticRule.objects.all()
    number_of_all_rules = allRules.__len__()
    number_of_chosen_rules = chosenRules.__len__()
    form = rulesForm()
    return render(request, 'Wordout/wordout_add.html', {
        'games': games,
        'chosenRules': chosenRules,
        'allRules': allRules,
        'gametype': gametype,
        'num_all_rules': number_of_all_rules,
        'num_chosen_rules': number_of_chosen_rules,
        'form': form
    })


# def wordout_add_distractor(request,pk):
#     gametype = GameType.objects.get(pk=pk)
#     games = Game.objects.filter(type=gametype)
#     chosenRules = AssociationTable.linguistic_rule_output.filter(gameType=gametype)
#     allRules = LinguisticRule.objects.all()
#     number_of_all_rules = allRules.__len__()
#     number_of_chosen_rules = chosenRules.__len__()
#     return render(request, 'Wordout/wordout_add.html', {
#         'games': games, 'chosenRules': chosenRules, 'allRules': allRules,
#         'gametype': gametype,
#         'num_all_rules': number_of_all_rules,
#         'num_chosen_rules': number_of_chosen_rules
#     })


# def wordout_add_question(request,pk):
#
#     return
