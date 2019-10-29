from django.urls import path

from . import views as goodbuyDatabase_views

app_name = "goodbuyDatabase"

urlpatterns = [
    path("new/product/", goodbuyDatabase_views.create_product, name="create_product"),
    path("add/product/<str:code>/", goodbuyDatabase_views.add_product, name="add_product"),
    path("product/<int:pk>/update/", goodbuyDatabase_views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/", goodbuyDatabase_views.ProductDeleteView.as_view(), name="product_delete"),
    path("list_all/", goodbuyDatabase_views.product_list, name="product_list"),
    path("list_codes/<list>/", goodbuyDatabase_views.show_list_of_codes, name="show_list_of_codes"),
    path("product/<int:pk>/details", goodbuyDatabase_views.ProductDetailView.as_view(), name="product_detail"),
    path("instant_feedback/<str:code>/", goodbuyDatabase_views.instant_feedback, name="instant_feedback"),
    path("is_in_own_database/<str:code>/", goodbuyDatabase_views.is_in_own_database, name="is_in_own_database"),
    path("saveproduct/", goodbuyDatabase_views.endpoint_saveproduct, name="endpoint_saveproduct"),
]
