# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import copy

import sys
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from Linguistics.forms import linguisticsRForm
from Linguistics.models import LinguisticRule
from Database.models import Dictionary, Entry, get_entries_that_match


def index(request):
    return render(request, 'Linguistics/index.html')


def linguistics_detail(request, pk):
    try:
        rule = LinguisticRule.objects.get(id=pk)
    except LinguisticRule.DoesNotExist:
        raise Http404("Rule does not exist")
    print >> sys.stderr, rule
    return render(request, 'Linguistics/linguistics_detail.html', {'rule': rule})


def linguistics_list(request):
    response = "Listing of Linguistic Rules."
    try:
        rules = LinguisticRule.objects.all()
    except LinguisticRule.DoesNotExist:
        raise Http404("rules do not exist")
    return render(request, "Linguistics/linguistics_list.html", {'rules': rules})


def linguistics_edit(request, pk):
    try:
        rule = get_object_or_404(LinguisticRule,pk=pk)
    except LinguisticRule.DoesNotExist:
        raise Http404("This rule does not exist")

    if request.method == "POST":
        form = linguisticsRForm(request.POST,instance=rule)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.save()
            print sys.stderr, rule.name, rule.pk
            return redirect('linguistics_detail', pk=rule.pk)
    else:
        form=linguisticsRForm(instance=rule)

    return render(request, 'Linguistics/linguistics_edit.html',{'form': form, 'rule': rule})


def linguistics_new(request):
    if request.method == "POST":
        form = linguisticsRForm(request.POST)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.save()
            print >> sys.stderr, "saved rule: ", rule.name
            return redirect('linguistics_detail', pk=rule.pk)
    else:
        form = linguisticsRForm()

    return render(request, 'Linguistics/linguistics_edit.html', {'form': form})


def linguistics_duplicate(request,pk):
    if request.method == "POST":
        form = linguisticsRForm(request.POST)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.save()
            return redirect('linguistics_list')
    else:
        rule = LinguisticRule.objects.get_or_create(pk=pk)[0]
        copy_rule = copy.copy(rule)
        print >> sys.stderr, "NEW name: ", copy_rule.name
        print >> sys.stderr, "NEW descrition ", copy_rule.description
        copy_rule.pk = None
        copy_rule.name = copy_rule.name + " (copy)"
        # copy_rule.save()
        # print >> sys.stderr, "NEW KEY", copy_rule.pk
        # copy_rule.refresh_from_db()
        # print >> sys.stderr, "NOW: ", copy_rule
        form = linguisticsRForm(instance=copy_rule)

    return render(request, 'Linguistics/linguistics_edit.html', {'form': form})

    # if request.method == "POST":
    #     form = linguisticsRForm(request.POST)
    #     if form.is_valid():
    #         rule = form.save(commit=False)
    #         rule.save()
    #         print >> sys.stderr, "saved rule: ", rule.name
    #         return redirect('linguistics_detail', pk=rule.pk)
    # else:
    #     form = linguisticsRForm()


def linguistics_delete(request,pk):
    try:
        rule = LinguisticRule.objects.get(pk=pk)
    except LinguisticRule.DoesNotExist:
        messages.warning(request, 'This rule no longer exists.')
        return redirect('linguistics_list')
    else:
        rule.delete()

    return redirect('linguistics_list')


def linguistics_Rulelist(request,pk):
    rule = LinguisticRule.objects.get(pk=pk)
    entries, message = get_entries_that_match(instance=rule)
    num_entries = len(entries)
    print >> sys.stderr, num_entries
    if (message != ""): messages.warning(request, message)

    return render(request, 'Linguistics/linguistics_Rulelist.html',
                  {'entries': entries, 'num_entries': num_entries, 'rule': rule})


