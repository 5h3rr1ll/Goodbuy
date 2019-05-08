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


        def save(self, commit=True):
            product = super(RegistrationFrom, self).save(commit=False)
            product.code = self.cleaned_data["code"]
            product.name = self.cleaned_data["name"]
            poduct.added_by = request.user
            if commit:
                product.save()
            return product
