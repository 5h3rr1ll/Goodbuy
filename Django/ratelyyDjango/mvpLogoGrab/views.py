from django.shortcuts import render, redirect
from mvpLogoGrab.forms import RegistrationForm

# Create your views here.
def home(request):
    numbers = [25,5,6,8]
    name = "Darjusch Schrand"
    args = { 'myName' : name, 'numbers' : numbers}
    return render(request, 'mvpLogoGrab/login.html', args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mvpLogoGrab")
        else:
            form = RegistrationForm()
            args = {"form": form}
            return render(request, "mvpLogoGrab/reg_failed.html", args)
    else:
        form = RegistrationForm()
        args = {"form": form}
        return render(request, "mvpLogoGrab/reg_form.html", args)
   