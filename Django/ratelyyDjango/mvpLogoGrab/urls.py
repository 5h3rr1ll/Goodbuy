from django.conf.urls import url
from mvpLogoGrab import views
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path

app_name = "logograb"

urlpatterns = [
    url(r'^$', views.snap, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='mvpLogoGrab/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='mvpLogoGrab/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^failed_register/$', views.register, name='failed_register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name="mvpLogoGrab/reset_password.html"), name='reset_password'),
    url(r'^reset-password/done$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^data/$', views.get_data, name='get_data'),
    url(r'^post/$', views.post, name='post'),
    url(r'^upload/$', views.upload, name='upload'),
    path('dataUrl/<dataurl>', views.dataUrl, name="dataurl"),

]
