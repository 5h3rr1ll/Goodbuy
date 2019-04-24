from django import forms
from ratelyyDatabase.models import Product, Brand

class AddNewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "code",
            "name",
            "brand",
            "concern",
            "main_category",
            "sub_category",
        ]
