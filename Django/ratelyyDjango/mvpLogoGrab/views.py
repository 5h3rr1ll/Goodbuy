from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationFrom,
    EditProfileForm,
)
# Create your views here.
def home(request):
    numbers = [25,5,6,8]
    name = "Darjusch Schrand"
    args = { 'myName' : name, 'numbers' : numbers}
    return render(request, 'mvpLogoGrab/login.html', args)

def register(request):
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mvpLogoGrab")
        else:
            form = RegistrationFrom()
            args = {"form": form}
            return render(request, "mvpLogoGrab/reg_failed.html", args)
    else:
        form = RegistrationFrom()
        args = {"form": form}
        return render(request, "mvpLogoGrab/reg_form.html", args)
