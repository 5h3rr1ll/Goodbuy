from django.shortcuts import render, redirect
from mvpScanWebApp import views
from ratelyyDatabase.models import Product
from mvpScanWebApp.forms import AddNewProductForm
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
    # form = AddNewProductForm(initial={"gtin":code})
    # args = {
    #     "code":code,
    #     "form":form,
    # }
    # return render(request, "mvpScanWebApp/add.html",args)

    if request.method == "POST":
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/gtin")
        else:
            return redirect("/accounts/profile")
    else:
        form = AddNewProductForm(initial={"gtin":code})
        args = {"form": form}
        return render(request, "accounts/reg_form.html", args)

def show(request, code):
    product = Product.objects.get(gtin=code)
    args = {
        "product":product
    }
    return render(request, "mvpScanWebApp/show.html",args)
