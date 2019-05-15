from django.shortcuts import render, redirect, render_to_response
from goodbuyDatabase.models import Product, Corporation, Rating
from codeScanner.forms import AddNewProductForm
from django.contrib.auth.models import User, Group

# Create your views here.

def scanCode(request):
    return render(request, "codeScanner/code.html")

def add(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            '''commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1'''
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                print("Worked")
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code")
            else:
                print("Doh!")
                product.checked = False
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
    corporation = Concern.objects.get(name=product.corporation)
    rating = Rating.objects.get(corporation=corporation.id)
    if rating.animals == None or rating.humans == None  or rating.environment == None:
        total_rating = 0
    else:
        total_rating = round((rating.animals+rating.humans+rating.environment)/3)*10
    args = {
        "product":product,
        "rating_result":total_rating,
        "rating":rating,
        "corporation":corporation,
    }
    return render(request, "codeScanner/rating.html",args)
