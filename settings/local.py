from .base import *

ALLOWED_HOSTS = ["127.0.0.1","localhost",]
DEBUG = True
DATABASES = {
    "default" : {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "local_goodbuy_db",
        "HOST": "127.0.0.1",
        "Port": "5432",
    }
}
