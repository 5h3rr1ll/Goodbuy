from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DetailView, ListView, DeleteView

from .forms import AddNewProductForm
from .models import Product


@login_required
def add_product(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)
        image = request.FILES["image"]
        print("Image Infos= Name:",image.name,"size:",image.size)
        if form.is_valid():
            '''commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1'''
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code")
            else:
                product.checked = False
                product.save()
                return redirect("/code")
        return render_to_response('goodbuyDatabase/add_product.html', {'form': form})
    else:
        try:
            product = Product.objects.get(code=code)
            product.scanned_counter += 1
            product.save()
            args = {
                "product":product,
            }
            return render(request,"goodbuyDatabase/product_already_exists.html",args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form":form,
                "error":e,
                }
            return render(request, "goodbuyDatabase/add_product.html", args)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        "name","code","image","brand","corporation","main_category",
        "sub_category","certificate",
        ]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_staff == post.added_by.is_staff:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = "/goodbuyDatabase/list_all/"

    def test_func(self):
        product = self.get_object()
        if self.request.user.is_staff:
            return True
        return False

@staff_member_required
def product_list(request):
    products = Product.objects.all()
    return render(
        request,
        "goodbuyDatabase/product_list.html",
        { "products":products })

def show_list_of_codes(request, list):
    lst2 = list.split(",")
    lst3 = []
    for x in lst2:
        if x not in lst3:
            lst3.append(x)
    args = {
        "list":lst3,
        }
    return render(request, "goodbuyDatabase/list_of_product_codes.html", args)

class ProductDetailView(DetailView):
    model = Product
