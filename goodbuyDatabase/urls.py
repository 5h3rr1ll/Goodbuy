from django.urls import path

from . import views as goodbuyDatabase_views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("add/<code>/", goodbuyDatabase_views.add_product, name="product_create"),
    path("products/<int:pk>/update/", goodbuyDatabase_views.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/", goodbuyDatabase_views.delete_product, name="product_delete"),
    path("products/", goodbuyDatabase_views.product_list, name="product_list"),
    path("product/<int:pk>/", goodbuyDatabase_views.ProductDetailView.as_view(), name="product_detail"),
]
