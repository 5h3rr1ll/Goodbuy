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
            "product_category",
            "product_sub_category",
        ]
