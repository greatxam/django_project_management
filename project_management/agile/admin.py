# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from django.contrib import admin

from agile.models import *


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
