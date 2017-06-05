# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from Linguistics.forms import linguisticsQForm, linguisticsRForm
from Linguistics.models import LinguisticRule, LinguisticQuestion


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



def linguistics_new(request,pk):
    form = linguisticsRForm()
    return render(request, 'Linguistics/linguistics_new.html')


