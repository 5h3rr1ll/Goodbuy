from django.urls import path
from collectDataApp import views

app_name = "collectDataApp"

urlpatterns = [
    path('', views.addProductView, name='addProductView'),
]
