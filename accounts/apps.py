# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # creates a userprofile when a user gets created
    def ready(self):
        import accounts.signals
