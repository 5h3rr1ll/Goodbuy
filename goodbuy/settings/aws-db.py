from .base import *

from os import environ

ALLOWED_HOSTS = [
    "*",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': environ.get('DATABASEUSER'),
        'NAME': environ.get('DATABASENAME'),
        'PASSWORD': environ.get('DATABASEPW'),
        'HOST': environ.get('DATABASEHOST'),
        'PORT': environ.get('DATABASEPORT'),
        }
    }