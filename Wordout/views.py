# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from Games.models import Game, GameType
from Linguistics.models import LinguisticRule
from Wordout.models import AssociationTable
from Database.models import Entry, get_entries_that_match

from Wordout.forms import associateForm, rulesForm
from Linguistics.forms import linguisticsRForm
from Database.forms import entryForm

# Create your views here.

def index(request):
    return render(request, 'Wordout/index.html')


def wordout_associate(request):
    gametypes = GameType.objects.all()
    return render(request, 'Wordout/wordout_associate.html', {'gametypes': gametypes} )

def wordout_list(request):
    return render(request, 'Wordout/wordout_list.html')

def wordout_print(request,pk):
    print >> sys.stderr, pk
    association = AssociationTable.objects.get(pk=pk)
    print >> sys.stderr, association
    entries = []
    distractors = []
    rule = LinguisticRule.objects.get(pk=association.linguistic_rule_input.pk)
    distractor = LinguisticRule.objects.get(pk=association.linguistic_rule_output.pk)
    entries = get_entries_that_match(rule)
    distractors = get_entries_that_match(distractor)
    return render(request, 'Wordout/wordout_print.html',
                  {'association': association, 'entries': entries, 'distractors': distractors})

def wordout_add_question(request,rpk,gpk,dpk):
    print >> sys.stderr, rpk, gpk, dpk
    gametype = GameType.objects.get(pk=gpk)
    rule = LinguisticRule.objects.get(pk=rpk)
    distractor = LinguisticRule.objects.get(pk=dpk)
    if request.method == 'POST':
        print >> sys.stderr, request.method
        question = request.POST.get('question')
        name = request.POST.get('name')
        association = AssociationTable.objects.create()
        association.name = name
        association.gameType = gametype
        association.linguistic_rule_input = rule
        association.linguistic_rule_output = distractor
        association.question = question
        association.save()
        print >> sys.stderr, association
        return redirect('wordout_print', pk=association.pk)

    rform = rulesForm()
    lform = linguisticsRForm(instance=rule)
    wform = entryForm()
    entries = []
    entries = get_entries_that_match(instance=rule)
    num_entries = entries.__len__()
    distractors = []
    distractors = get_entries_that_match(instance=distractor)
    num_distractors = distractors.__len__()

    return render(request, 'Wordout/wordout_add_question.html',
                  {'gametype': gametype, 'rule': rule,
                   'rform': rform, 'lform': lform,
                   'entries': entries, 'wform': wform,'num_entries': num_entries,
                   'distractor': distractor,
                   'distractors': distractors, 'num_distractors': num_distractors
                   })

def wordout_add_distractor(request, rpk, gpk):
    print >> sys.stderr, rpk, gpk
    gametype = GameType.objects.get(pk=gpk)
    rule = LinguisticRule.objects.get(pk=rpk)
    if request.method == 'POST':
        distractor = request.POST.get('rules')
        return redirect('wordout_add_question', rpk=rpk, gpk=gpk, dpk=distractor)


    rform = rulesForm()
    lform = linguisticsRForm(instance=rule)
    wform = entryForm()
    entries = []
    entries = get_entries_that_match(instance=rule)
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
def wordout_association_list(request):
    associations = AssociationTable.objects.all()
    return render(request, 'Wordout/wordout_association_list.html',{'associations': associations})