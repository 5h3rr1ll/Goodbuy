from django.urls import path
from goodbuyDatabase import views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("add/<code>", views.add, name="add"),
]
