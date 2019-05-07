from django.urls import path
from mvpScanWebApp import views

app_name = "gtin"

urlpatterns = [
    path('', views.gtin, name='gtin'),
    path("add/<code>", views.add, name="add"),
    path("show/<code>", views.show, name="show"),
]
