from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name = 'mvpLogoGrab/login.html'), name = 'login'),
    url(r'^logout/$', LogoutView.as_view(template_name = 'mvpLogoGrab/logout.html'), name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^failed_register/$', views.register, name='failed_register')
]