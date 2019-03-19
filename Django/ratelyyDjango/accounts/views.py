# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationFrom,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
# All logic goes thru the views. If you want to access e.g. data from a database
# you do it here in the view.py in the functions
def home(request):
    numbers = [1,2,3,4,5]
    name = "Anthony Sherrill"

    # myname is the name we will use in the template and the value in the
    # dict is the variable within this function
    # args takes all variabels you want to display on the rendered site
    args = {"myName": name, "numbers": numbers}
    return render(request, "accounts/home.html", args)

def register(request):
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account")
    else:
        form = RegistrationFrom()

        args = {"form": form}
        return render(request, "accounts/reg_form.html", args)

def view_profile(request):
    args = {"user": request.user}
    return render(request, "accounts/profile.html", args)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("/account/profile")
    else:
        form = EditProfileForm(instance = request.user)
        args = {"form": form}
        return render(request, "accounts/edit_profile.html", args)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/account/profile")
        else:
            return redirect("/account/change-password")
    else:
        form = PasswordChangeForm(user = request.user)
        args = {"form": form}
        return render(request, "accounts/change_password.html", args)