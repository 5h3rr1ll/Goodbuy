from django.shortcuts import render, redirect, render_to_response
from goodbuyDatabase.models import Product, Corporation, Rating
from django.contrib.auth.models import User, Group

# Create your views here.

def scanCode(request):
    return render(request, "codeScanner/code.html")
