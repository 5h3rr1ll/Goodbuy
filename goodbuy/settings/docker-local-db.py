import os

from .base import *


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        # host.docker.internal is a special DNS name that resolves to the internal IP address used by the host.
        "HOST": "host.docker.internal",
        "PORT": "5432",
        "USER": "anthony",
    }
}

os.environ["PGDATA"] = f'{DATABASES["default"]["HOST"]}/var/lib/postgresql/data/pgdata'