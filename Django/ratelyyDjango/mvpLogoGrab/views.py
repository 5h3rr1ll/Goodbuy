from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mvpLogoGrab.forms import RegistrationForm
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
    numbers = [25,5,6,8]
    name = "Darjusch Schrand"
    args = {'myName' : name, 'numbers' : numbers}
    return render(request, 'mvpLogoGrab/login.html', args)

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
        form = UserChangeForm(request.POST, instane=request.user)
        if form.is_valid():
            form.save()
            return redirect('/mvpLogoGrab/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {"form": form}
        return render(request, 'mvpLogoGrab/edit_profile.html', args)