from django import forms
from ratelyyDatabase.models import Product

class AddNewProductForm(forms.ModelForm):
    code = forms.IntegerField(required=True)
    name = forms.CharField(required=True,strip=True)

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
