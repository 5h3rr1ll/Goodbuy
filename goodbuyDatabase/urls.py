from django.urls import path

from . import views as goodbuyDatabase_views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("products/", goodbuyDatabase_views.ProductListView.as_view(), name="product_list"),
    path("product/<code>/new/", goodbuyDatabase_views.add_product, name="product_create_by_codescanner"),
    path("product/new/", goodbuyDatabase_views.ProductCreatView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", goodbuyDatabase_views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", goodbuyDatabase_views.ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/", goodbuyDatabase_views.ProductDetailView.as_view(), name="product_detail"),
    path("products/<str:username>/", goodbuyDatabase_views.UserProductListView.as_view(), name="user_products"),
]
