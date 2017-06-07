# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from Levels.models import WordLevels, CVCLevels, LetterLevels, Level

from Levels.forms import levelForm, letterForm, CVCForm

from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'Levels/index.html')


def level_list(request):
    letter_levels = Level.objects.filter(type='letter').order_by('level')
    CVC_levels = Level.objects.filter(type='CVC').order_by('level')
    print >> sys.stderr, CVC_levels
    return render(request, 'Levels/level_list.html',
                  {'letter_levels': letter_levels, 'CVC_levels': CVC_levels}
                  )


def level_detail(request,pk):
    try:
        level = Level.objects.get(id=pk)
    except Level.DoesNotExist:
        raise Http404("Rule does not exist")
    print >> sys.stderr, level
    return render(request, 'Levels/level_detail.html', {'level': level})


def level_edit(request,pk):
    print >> sys.stderr, "made it to edit"
    try:
        level = get_object_or_404(Level,pk=pk)
    except Level.DoesNotExist:
        raise Http404("This level does not exist")

    if request.method == "POST":
        form = levelForm(request.POST,instance=level)
        if form.is_valid():
            level = form.save(commit=False)
            level.save()
            print sys.stderr, level.name, level.pk
            return redirect('level_list')
    else:
        form=levelForm(instance=level)

    return render(request, 'Levels/level_edit.html',{'form': form})


def level_new(request,id):
    form = 'hello'
    id = int(id)
    type = 'unknown'
    if (id == 1): type = 'letter'
    if (id == 2): type = 'CVC'

    if request.method == "POST":
        form = levelForm(request.POST)
        if form.is_valid():
            level = form.save(commit=False)
            level.type = type
            level.save()
            print >> sys.stderr, "saved rule: ", level.name
            return redirect('level_list')
            # return redirect(request, 'Levels/level_list.html')
    else:
        form = levelForm()

    print >> sys.stderr, form, id
    return render(request, 'Levels/level_edit.html', {'form': form})


def level_delete(request,pk):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        messages.warning(request, 'This level no longer exists.')
        return redirect('level_list')
    else:
        level.delete()

    return redirect('level_list')


