from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

app_name = "accounts"

class PasswordResetView2(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')

class PasswordResetDoneView2(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirmView2(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')

class PasswordResetCompleteView2(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("reset-password/", PasswordResetView2.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
    path("reset-password/done/", PasswordResetDoneView2.as_view(), name="password_reset_done"),
    path("reset-password/confirm/<uidb64><token>/", PasswordResetConfirmView2.as_view(), name="password_reset_confirm"),
    path("reset-password/complete/", PasswordResetCompleteView2.as_view(), name="password_reset_complete"),
]
