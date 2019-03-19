from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class RegistrationForm(UserCreationForm):
    email = models.EmailField(requierd=True)