# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from rest_framework import serializers

from agile.models import *


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = '__all__'
