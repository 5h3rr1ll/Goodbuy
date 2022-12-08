from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.environ.get("DATABASEUSER"),
        'NAME': os.environ.get("DATABASENAME"),
        'PASSWORD': os.environ.get("DATABASEPW"),
        'HOST': os.environ.get("DATABASEHOST"),
        'PORT': os.environ.get("DATABASEPORT"),
        }
    }