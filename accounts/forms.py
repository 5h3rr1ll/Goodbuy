from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    # password1 = forms.CharField(min_length=7)

    class Meta:
        model = User
        # in fields you declare which fields will be displayed at the RegForm
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            "email",
            "first_name",
            "last_name",
            "password",
        }
