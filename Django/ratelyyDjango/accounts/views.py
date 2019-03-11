# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account")
    else:
        form = UserCreationForm()

        args = {"form": form}
        return render(request, "accounts/reg_form.html", args)
