# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#             user_profile = AuthUser.objects.create(user=kwargs["instance"])
#
# post_save.connect(create_profile, sender=User)
