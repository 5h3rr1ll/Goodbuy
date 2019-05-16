from django.urls import path

from goodbuyDatabase import views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("add/<code>/", views.add_product, name="add_product"),
    # TODO: 
    # path("products/update/<int:pk>/", views.update_product, name="product_update"),
    path("products/<int:pk>/", views.delete_product, name="delete_product"),
    path("products/", views.product_list, name="product_list"),
]
