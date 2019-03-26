from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mvpLogoGrab.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import requests

# Create your views here.
def home(request):
    numbers = [25,5,6,8]
    name = "Darjusch Schrand"
    args = {'myName' : name, 'numbers' : numbers}
    return render(request, 'mvpLogoGrab/home.html', args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mvpLogoGrab/profile")
        else:
            form = RegistrationForm()
            args = {"form": form}
            return render(request, "mvpLogoGrab/reg_failed.html", args)
    else:
        form = RegistrationForm()
        args = {"form": form}
        return render(request, "mvpLogoGrab/reg_form.html", args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'mvpLogoGrab/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/mvpLogoGrab/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, 'mvpLogoGrab/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/mvpLogoGrab/profile')
        else:
            return redirect('/mvpLogoGrab/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {"form": form}
        return render(request, 'mvpLogoGrab/change_password.html', args)

def logo_grab(request):

    url = "https://api.logograb.com/detect"

    querystring = {"mediaUrl":"http://s3.logograb.com/pub/test.png","developerKey":"nb9n3ra9fpmrk0u0binh2b03jr3acq510tqhldmr"}

    response = requests.request("POST", url, params=querystring)

    args = {"response": response}
    return render(request, 'mvpLogoGrab/logo_grab.html', args)