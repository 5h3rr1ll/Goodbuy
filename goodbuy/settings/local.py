import os

from .base import *

os.system("pg_ctl -D /usr/local/var/postgres start")


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "HOST": "127.0.0.1",
        "Port": "5432",
    }
}
