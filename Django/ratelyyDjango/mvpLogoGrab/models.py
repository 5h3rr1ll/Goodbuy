from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserLogoProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserLogoProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
