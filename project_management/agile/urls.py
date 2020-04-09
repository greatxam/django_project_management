# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from agile import views

urlpatterns = [
    # values
    path('values/', views.ValueListAPIView.as_view(), name='agile-api-value-list'),
    path('values/<uuid:pk>/', views.ValueDetailAPIView.as_view(), name='agile-api-value-detail'),

    # principles
    path('principles/', views.PrincipleListAPIView.as_view(), name='agile-api-principle-list'),
    path('principles/<uuid:pk>/', views.PrincipleDetailAPIView.as_view(), name='agile-api-principle-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
