# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from rest_framework import generics
from rest_framework.permissions import AllowAny

from agile.serializers import *
from agile.models import *


class ValueListAPIView(generics.ListCreateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = [AllowAny]


class ValueDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = [AllowAny]


class PrincipleListAPIView(generics.ListCreateAPIView):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    permission_classes = [AllowAny]


class PrincipleDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    permission_classes = [AllowAny]
