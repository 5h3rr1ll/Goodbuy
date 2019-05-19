from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . import views as accounts_view


app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="accounts/login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(
        template_name="accounts/logout.html"),
        name="logout"),
    path("register/", accounts_view.register, name="register"),
    path("user_profile/", accounts_view.user_profile, name="user_profile"),
    path("user_profile/edit/",
        accounts_view.edit_user_profile,
        name="edit_user_profile"),
    path("change-password/",
        accounts_view.change_password,
        name="change_password"),
    path("reset-password/",
        PasswordResetView.as_view(
            template_name="accounts/password_reset.html"),
        name="password_reset"),
    path("reset-password/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    path("reset-password/confirm/<uidb64><token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),
    path("reset-password/complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),
]
