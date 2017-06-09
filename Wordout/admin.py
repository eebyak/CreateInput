# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Wordout.models import AssociationTable

# Register your models here.


class AssociationInline(admin.TabularInline):
    model = AssociationTable
    extra = 3


class AssociationAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,
    {'fields': ['name','gameType','question']}
    ),
                ]
    # inlines = [RuleInline]

admin.site.register(AssociationTable,AssociationAdmin)