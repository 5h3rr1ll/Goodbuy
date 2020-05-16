
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, DetailView, UpdateView

from .forms import AddNewProductForm
from .models import Product


def create_product_form(request):
    if request.method == "POST" and request.is_ajax():
        form = AddNewProductForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        image = request.POST["image"].replace("C:\\fakepath\\", "product_image/")
        print("Image path:", image)
        if form.is_valid():
            print(request.POST)
            name = request.POST["name"]
            code = request.POST["code"]
            # TODO: use get_or_create() to add Brand or corporation
            # product.name = request.POST["name"]

            Product.objects.create(
                name=name, code=code, image=image,
            )
        else:
            print("\n!!! error While creating Product !!!\n")
        return HttpResponse("")
    else:
        form = AddNewProductForm(request.POST)
        return render(request, "goodbuyDatabase/add_product_form.html", {"form": form})
        print("\n!!! error While creating Product !!!\n")
    return HttpResponse("")


# @login_required
def add_product_form(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)

        if form.is_valid():
            """
            commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1
            """
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code_scanner/")
            else:
                product.checked = False
                product.save()
                return redirect("/code_scanner/")
        return render(request, "goodbuyDatabase/add_product_form.html", {"form": form})
    else:
        try:
            product = Product.objects.get(code=code)
            product.scanned_counter += 1
            product.save()
            args = {
                "product": product,
            }
            return render(request, "goodbuyDatabase/product_already_exists.html", args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code": code})
            args = {
                "form": form,
                "error": e,
            }
            return render(request, "goodbuyDatabase/add_product_form.html", args)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        "name",
        "code",
        "image",
        "brand",
        "corporation",
        "main_category",
        "sub_category",
        "certificate",
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
        if self.request.user.is_staff:
            return True
        return False


def product_list(request):
    products = Product.objects.all()
    return render(request, "goodbuyDatabase/product_list.html", {"products": products})


def show_list_of_codes(request, list, *args, **kwargs):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)
        if form.is_valid():
            """
            commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1
            """
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code_scanner/")
            else:
                product.checked = False
                product.save()
    else:
        single_codes = list.split(",")
        product_in_db = []
        product_not_in_db = []

        for code in single_codes:
            try:
                product = Product.objects.get(code=code)
                product_in_db.append(product)
            except Exception:
                print(str(Exception))
                form = AddNewProductForm(initial={"code": code})
                product_not_in_db.append(form)

        args = {
            "allready_in_db": product_in_db,
            "product_not_in_db": product_not_in_db,
        }
        return render(request, "goodbuyDatabase/list_of_product_codes.html", args)


class ProductDetailView(DetailView):
    model = Product


def loaderio(request):
    return render(request, "goodbuyDatabase/loaderio.html")
