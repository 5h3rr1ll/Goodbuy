# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city="Berlin")

class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    description = models.TextField(max_length=140, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(default="",null=True, blank=True)
    phone = models.CharField(max_length=17, null=True, blank=True)
    image = models.ImageField(
        default="default.jpg",
        upload_to="profile_image",
        blank=True)

    # this UserProfileManager instance cause a error by creating profile when creating
    # new user
    # berlin = UserProfileManager()

    def __str__(self):
        return f"{self.user.username} Profile"

    class Meta:
        managed = True
        db_table = 'user_profiles'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs["instance"])

post_save.connect(create_profile, sender=User)
