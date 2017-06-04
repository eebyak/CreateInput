# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from Database.admin import EntryInline
from Games.models import Game, GameType


# Register your models here.

class GameInline(admin.TabularInline):
    model = Game
    extra = 3


class GameTypeAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,
             {'fields': ['name']}
             ),
                ]
    inlines = [GameInline]

admin.site.register(GameType,GameTypeAdmin)