from django.urls import path, re_path
from mvpScanWebApp import views


app_name = "mvpScanWebApp"

urlpatterns = [
    path('', views.gtin, name='home'),
    path('search', views.searchResult, name='searchResult'),
]
