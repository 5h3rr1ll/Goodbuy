# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm, EditProfileForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! Your are now able to log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form":form})

# This is a decorator, you can place them infront of a function to e.g. require
# that a user needed to be logged in to use that function
@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {"user": user}
    return render(request, "accounts/profile.html", args)

@login_required
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

@login_required
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
