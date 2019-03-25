from django.conf.urls import url
from mvpScanWebApp import views

app_name = "mvpScanWebApp"

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
