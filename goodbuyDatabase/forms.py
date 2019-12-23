from django import forms

from .models import Product


class AddNewProductForm(forms.ModelForm):
    code = forms.IntegerField(required=True)
    name = forms.CharField(required=True, strip=True)

    class Meta:
        model = Product
        fields = [
            "code",
            "name",
            "image_of_front",
            "image_of_details",
            "brand",
            "main_product_category",
            "product_category",
            "sub_product_category"
        ]
