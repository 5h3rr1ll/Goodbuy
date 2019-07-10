from django.urls import path

from . import views as goodbuyDatabase_views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("new/product/", goodbuyDatabase_views.create_product, name="create_product"),
    path("product/<int:pk>/update/", goodbuyDatabase_views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/", goodbuyDatabase_views.ProductDeleteView.as_view(), name="product_delete"),
    path("list_all/", goodbuyDatabase_views.product_list, name="product_list"),
    path("list_codes/<list>/", goodbuyDatabase_views.show_list_of_codes, name="show_list_of_codes"),
    path("product/<int:pk>/details", goodbuyDatabase_views.ProductDetailView.as_view(), name="product_detail"),
]
