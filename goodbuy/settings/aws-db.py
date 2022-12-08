from .base import *

ALLOWED_HOSTS = [
    "*",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': "postgres",
        'NAME': "goodbuy",
        'PASSWORD': "Nix123456",
        'HOST': "goodbuy-db.cmzadqebmwup.eu-central-1.rds.amazonaws.com",
        'PORT': '5432',
        }
    }