# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
    UserRegisterForm,
    EditProfileForm,
    UserPorfileUpdateForm,
    UserUpdateForm,)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! Your are now able to log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form":form})

# This is a decorator, you can place them infront of a function to e.g. require
# that a user needed to be logged in to use that function
@login_required
def user_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserPorfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("user_profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserPorfileUpdateForm(instance=request.user.userprofile)

    context = {
    "u_form": u_form,
    "p_form": p_form
    }

    return render(request, "accounts/user_profile.html", context)

@login_required
def edit_user_profile(request):
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
