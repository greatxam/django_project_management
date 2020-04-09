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


class PrincipleTestHelper:
    API_LIST_PRINCIPLE = 'agile-api-principle-list'
    API_DETAIL_PRINCIPLE = 'agile-api-principle-detail'

    @staticmethod
    def get_principle(name):
        return get_object_or_404(Principle, name=name)

    @staticmethod
    def create_principle(name, description):
        return Principle.objects.create(name=name, description=description)
