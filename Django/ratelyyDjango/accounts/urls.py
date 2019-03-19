from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
LoginView,
LogoutView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
)

urlpatterns = [
    url(r"^$", views.home),
    url(r"^login/$", LoginView.as_view(template_name="accounts/login.html"), name="Alogin"),
    url(r"^logout/$", LogoutView.as_view(template_name="accounts/logout.html"), name="Alogout"),
    url(r"^register/$", views.register, name="Aregister"),
    url(r"^profile/$", views.view_profile, name="Aview_profile"),
    url(r"^profile/edit/$", views.edit_profile, name="Aedit_profile"),
    url(r"^change-password/$", views.change_password, name="Achange_password"),
    url(r"^reset-password/$", PasswordResetView.as_view(template_name="accounts/reset_password.html"), name="reset_password"),
    url(r"^reset-password/done/$", PasswordResetDoneView.as_view(), name="Apassword_reset_done"),
    url(r"^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetConfirmView.as_view(), name="Apassword_reset_confirm"),
    url(r"^reset-password/complete/$", PasswordResetCompleteView.as_view(), name="Apassword_reset_complete"),
]
