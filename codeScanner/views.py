from django.shortcuts import render, redirect, render_to_response
from goodbuyDatabase.models import Product, Corporation, Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


@login_required
def scanCode(request):
    return render(request, "codeScanner/code.html")
