from django.shortcuts import render, redirect, render_to_response
from ratelyyDatabase.models import Product, Concern, Rating
from codeScanner.forms import AddNewProductForm

# Create your views here.

def scanCode(request):
    return render(request, "codeScanner/code.html")

def add(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            '''commit=False allows you to modify the resulting object before it is
            actually saved to the database. Source: https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1'''
            product = form.save(commit=False)
            product.added_by = request.user

            product.save()
            return redirect("/code")
        return render_to_response('codeScanner/add.html', {'form': form})
    else:
        try:
            product = Product.objects.get(code=code)
            product.scanned_counter += 1
            product.save()
            args = {
                "product":product,
            }
            return render(request,"codeScanner/show_already_exists.html",args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form":form,
                "error":e,
                }
            return render(request, "codeScanner/add.html", args)

def rating(request, code):
    product = Product.objects.get(code=code)
    concern = Concern.objects.get(name=product.concern)
    rating = Rating.objects.get(concern=concern.id)
    if rating.animals == None or rating.humans == None  or rating.environment == None:
        total_rating = 0
    else:
        total_rating = round((rating.animals+rating.humans+rating.environment)/3)*10
    args = {
        "product":product,
        "rating_result":total_rating,
        "rating":rating,
        "concern":concern,
    }
    return render(request, "codeScanner/rating.html",args)
