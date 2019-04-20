from django.shortcuts import render
from mvpScanWebApp import views
from ratelyyDatabase.models import Product
# Create your views here.

def gtin(request):
    numbers = [1,2,3,4,5]
    name = "Anthony Sherrill"

    # myname is the name we will use in the template and the value in the
    # dict is the variable within this function
    # args takes all variabels you want to display on the rendered site
    args = {
        "myName": name, "numbers": numbers
    }
    return render(request, "mvpScanWebApp/gtin.html", args)

def add(request, code):
    text = "Here should become something added"
    print(request)
    args = {
        "text":text,
        "code":code,
    }
    return render(request, "mvpScanWebApp/add.html",args)

def show(request, code):
    product = Product.objects.get(gtin=code)
    args = {
        "product":product
    }
    return render(request, "mvpScanWebApp/show.html",args)
