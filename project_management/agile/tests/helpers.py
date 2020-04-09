# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from agile.models import *
from django.shortcuts import get_object_or_404


class ValueTestHelper:
    API_LIST_VALUE = 'agile-api-value-list'
    API_DETAIL_VALUE = 'agile-api-value-detail'

    @staticmethod
    def get_value(name):
        return get_object_or_404(Value, name=name)

    @staticmethod
    def create_value(name, description):
        return Value.objects.create(name=name, description=description)
