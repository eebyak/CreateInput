# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Levels.models import Level
# Register your models here.



class LevelInline(admin.TabularInline):
    model = Level
    extra = 3


class LevelAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,
             {'fields': ['name','type','list','level']}
             ),
                ]
    # inlines = [LevelInline]

admin.site.register(Level,LevelAdmin)