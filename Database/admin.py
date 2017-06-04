# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dictionary, Entry

# Register your models here.


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 3


class DictionaryAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,
             {'fields': ['language']}
             ),
                ]
    inlines = [EntryInline]

admin.site.register(Dictionary,DictionaryAdmin)