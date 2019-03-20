from django.conf.urls import url
from mvpLogoGrab import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name = 'mvpLogoGrab/login.html'), name = 'login'),
    url(r'^logout/$', LogoutView.as_view(template_name = 'mvpLogoGrab/logout.html'), name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^failed_register/$', views.register, name='failed_register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change_password'),
]