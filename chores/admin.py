# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import ChoreList,Chore


class Chores(admin.TabularInline):
    model = Chore
    extra = 2

class ChoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Info', {'fields': ['due_date'], 'classes': ['collapse']})
    ]
    inlines = [Chores]

admin.site.register(ChoreList,ChoreAdmin)
