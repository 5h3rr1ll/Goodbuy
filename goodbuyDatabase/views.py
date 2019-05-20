from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    )

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

class ProductCreatView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["name","code"]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

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
        if self.request.user == post.added_by:
            return True
        return False

# @login_required
# def delete_product(request, pk):
#     if request.method == "POST":
#         product = Product.objects.get(pk=pk)
#         product.delete()
#     return redirect("goodbuyDatabase:product_list")

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = "/"

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.added_by:
            return True
        return False

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, "goodbuyDatabase/product_list.html", {
        "products":products
    })

class ProductListView(ListView):
    model = Product
    template_name = "goodbuyDatabase/product_list.html"
    context_object_name = "products"
    # the minus infront of date_posted bringst the newst post to the top
    ordering = ["-created"]
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product

class UserProductListView(ListView):
    model = Product
    template_name = "goodbuyDatabase/user_products.html"
    context_object_name = "products"
    # the minus infront of date_posted bringst the newst post to the top
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Product.objects.filter(added_by=user).order_by("-date_posted")
