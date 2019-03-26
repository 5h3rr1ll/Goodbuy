from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    # needed to uncommand this line because otherweise the input field appears
    # twice
    # Foo = forms.CharField()

    class Meta:
        model = Post
        fields = ("post",)
