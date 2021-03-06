# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import logging

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from Games.forms import gameForm, gametypeForm
from Games.models import Game, GameType

logging.basicConfig(format='%(message)s')

#    print >> sys.stderr, "item: ", item
def index(request):
    return render(request, 'Games/index.html')

# def gametype_detail(request, pk):
#     return render(request, 'Games/gametype_detail.html')

def gametype_detail(request, pk):
    try:
        gametype = GameType.objects.get(id=pk)
    except GameType.DoesNotExist:
        raise Http404("Gametype does not exist")
    #print >> sys.stderr, gametype
    return render(request, 'Games/gametype_detail.html', {'gametype': gametype})

def game_detail(request, pk):
    try:
        game = Game.objects.get(id=pk)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    #print >> sys.stderr, game
    return render(request, 'Games/game_detail.html', {'game': game})

def game_list(request):
    response = "Listing of Games."
    # form = gameForm()
    try:
        games = Game.objects.all()
    except Game.DoesNotExist:
        raise Http404("Games do not exist")
    return render(request, "Games/game_list.html", {'games': games})


def gametype_list(request):
    response = "Listing of Gametypes."
    # form = gameForm()
    try:
        gametypes = GameType.objects.all()
    except GameType.DoesNotExist:
        raise Http404("Gametype do not exist")
    return render(request, "Games/gametype_list.html", {'gametypes': gametypes})


def game_edit(request, pk):
    try:
        game = get_object_or_404(Game,pk=pk)
    except Game.DoesNotExist:
        raise Http404("This game does not exist")

    if request.method == "POST":
        form = gameForm(request.POST,instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            #print sys.stderr, game.name, game.pk
            return redirect('game_detail', pk=game.pk)
    else:
        form=gameForm(instance=game)

    return render(request, 'Games/game_edit.html',{'form': form, 'game': game})

def gametype_edit(request, pk):
    try:
        gametype = get_object_or_404(GameType,pk=pk)
    except GameType.DoesNotExist:
        raise Http404("This gametype does not exist")

    if request.method == "POST":
        form = gametypeForm(request.POST,instance=gametype)
        if form.is_valid():
            gametype = form.save(commit=False)
            gametype.save()
            #print sys.stderr, gametype.name, gametype.pk
            return redirect('gametype_detail', pk=gametype.pk)
    else:
        form=gametypeForm(instance=gametype)

    return render(request, 'Games/gametype_edit.html',{'form': form, 'gametype': gametype})



def game_new(request):
    if request.method == "POST":
        form = gameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            print >> sys.stderr, "saved rule: ", game.name
            return redirect('game_detail', pk=game.pk)
    else:
        form = gameForm()

    return render(request, 'Games/game_edit.html', {'form': form})


def game_delete(request,pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        messages.warning(request, 'This game no longer exists.')
        return redirect('game_list')
    else:
        game.delete()

    return redirect('game_list')


def gametype_new(request):
    if request.method == "POST":
        form = gametypeForm(request.POST)
        if form.is_valid():
            gametype = form.save(commit=False)
            gametype.save()
            #print >> sys.stderr, "saved gametype: ", gametype.name
            return redirect('gametype_detail', pk=gametype.pk)
    else:
        form = gametypeForm()

    return render(request, 'Games/gametype_edit.html', {'form': form})


def gametype_delete(request,pk):
    try:
        gametype = GameType.objects.get(pk=pk)
    except GameType.DoesNotExist:
        messages.warning(request, 'This game no longer exists.')
        return redirect('gametype_list')
    else:
        gametype.delete()

    return redirect('gametype_list')

