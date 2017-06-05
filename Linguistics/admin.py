# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from Database.admin import EntryInline
from Linguistics.models import LinguisticRule, LinguisticQuestion


# Register your models here.

class RuleInline(admin.TabularInline):
    model = LinguisticRule
    extra = 3


class LinguisticRuleAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,
    {'fields': ['name']}
    ),
                ]
    # inlines = [RuleInline]

admin.site.register(LinguisticRule,LinguisticRuleAdmin)