from django.urls import path
from mvpScanWebApp import views

app_name = "mvpScanWebApp"

urlpatterns = [
    path('', views.gtin, name='home'),
]
