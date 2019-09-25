from django.shortcuts import render, redirect
from goodbuyDatabase.models import Product, Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def scanCode(request):
    return render(request, "codeScanner/code_scanner.html")
