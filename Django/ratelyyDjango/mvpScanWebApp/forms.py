from django import forms
from ratelyyDatabase.models import Product, Brand

class AddNewProduct(forms.ModelForm):
    # gtin = forms.IntegerField()
    # name = forms.CharField(max_length=50)
    # brand = forms.AutoCompleteSelectField(lookup_class=Brand)
    # concern = forms.CharField(max_length=50)

    class Meta:
        model = Product
        fields = [
            "gtin",
            "name",
            "brand",
            "concern",
            "main_category",
            "sub_category",
        ]

    def save(self, commit=True):
        product = super(AddNewProduct, self).save(commit=False)
        product.gtin = self.cleaned_data["gtin"]
        product.name = self.cleaned_data["name"]

        if commit:
            product.save()
        return product
