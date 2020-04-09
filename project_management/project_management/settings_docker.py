# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'agile_pm_db',
        'USER': 'agile_pm_dba',
        'PASSWORD': 'WnVHKkyR2pW88TMY',
        'HOST': 'db',
        'PORT': 5432
    }
}
