# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from accounts.models import UserProfile
from django.contrib import admin

# Register your models here.

class UserProfileManager(models.Manager):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "user_info","city","phone","website")

    def user_info(self, objc):
        return objc.description

    user_info.short_description  = "Info"

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        # second or the further parameter(s) become used if the first is not clear
        queryset = queryset.order_by("-phone","-user","city")
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
