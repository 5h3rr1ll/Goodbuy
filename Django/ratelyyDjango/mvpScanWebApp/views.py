from django.shortcuts import render, redirect
from mvpScanWebApp import views
from ratelyyDatabase.models import Product
from mvpScanWebApp.forms import AddNewProductForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def gtin(request):
    return render(request, "mvpScanWebApp/gtin.html")

def add(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/gtin")
        else:
            # TODO: need a better logic for too long codes inserted
            return render(request,"mvpScanWebApp/error.html")
    else:
        if Product.objects.filter(code__contains=code).count() > 0:
            products = Product.objects.filter(code__contains=code)
            args = {
                "products":products,
            }
            return render(request,"mvpScanWebApp/show.html",args)
        else:
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form": form,
                }
            return render(request, "mvpScanWebApp/add.html", args)

def show(request, code):
    products = Product.objects.filter(code__contains=code)
    print(products)
    args = {
        "products":products,
    }
    return render(request, "mvpScanWebApp/show.html",args)
