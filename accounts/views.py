# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationFrom,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")
        else:
            return redirect("/accounts/register")
    else:
        form = RegistrationFrom()

        args = {"form": form}
        return render(request, "accounts/reg_form.html", args)

# This is a decorator, you can place them infront of a function to e.g. require
# that a user needed to be logged in to use that function
# @login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {"user": user}
    return render(request, "accounts/profile.html", args)

# @login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")
    else:
        form = EditProfileForm(instance = request.user)
        args = {"form": form}
        return render(request, "accounts/edit_profile.html", args)

# @login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/accounts/profile")
        else:
            return redirect("/accounts/change-password")
    else:
        form = PasswordChangeForm(user = request.user)
        args = {"form": form}
        return render(request, "accounts/change_password.html", args)