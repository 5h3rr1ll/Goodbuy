from django.shortcuts import render, redirect, render_to_response
from goodbuyDatabase.forms import AddNewProductForm
from goodbuyDatabase.models import Product

def add(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)
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
        return render_to_response('goodbuyDatabase/add.html', {'form': form})
    else:
        try:
            product = Product.objects.get(code=code)
            product.scanned_counter += 1
            product.save()
            args = {
                "product":product,
            }
            return render(request,"goodbuyDatabase/show_already_exists.html",args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form":form,
                "error":e,
                }
            return render(request, "goodbuyDatabase/add.html", args)

def product_list(request):
    products = Product.objects.all()
    return render(request, "goodbuyDatabase/product_list.html", {
        "products":products
    })

def delete_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.delete()
    return redirect("goodbuyDatabase:product_list")
