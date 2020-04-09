# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

import uuid

from django.db import models


class Value(models.Model):
    class Meta:
        db_table = 'agile_values'
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
