from django.urls import path
from goodbuyDatabase import views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("add/<code>/", views.add, name="add"),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:pk>/", views.delete_product, name="delete_product"),
]
