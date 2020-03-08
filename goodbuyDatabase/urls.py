from django.urls import path

from . import views as goodbuyDatabase_views
from . import endpoints as goodbuyDatabase_endpoints

app_name = "goodbuyDatabase"

urlpatterns = [
    path("new/product/", goodbuyDatabase_views.create_product_form, name="create_product_form"),
    path(
        "add/product/<str:code>/", goodbuyDatabase_views.add_product_form, name="add_product_form"
    ),
    path(
        "product/<int:pk>/update/",
        goodbuyDatabase_views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/",
        goodbuyDatabase_views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("list_all/", goodbuyDatabase_views.product_list, name="product_list"),
    path(
        "list_codes/<list>/",
        goodbuyDatabase_views.show_list_of_codes,
        name="show_list_of_codes",
    ),
    path(
        "product/<int:pk>/details",
        goodbuyDatabase_views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "is_in_own_database/<str:code>/",
        goodbuyDatabase_endpoints.is_in_own_database,
        name="is_in_own_database",
    ),
    path(
        "save_product/",
        goodbuyDatabase_endpoints.endpoint_save_product,
        name="endpoint_save_product",
    ),
    path(
        "update_product/",
        goodbuyDatabase_endpoints.endpoint_update_product,
        name="endpoint_update_product",
    ),
    path(
        "save_brand/",
        goodbuyDatabase_endpoints.endpoint_save_brand,
        name="endpoint_save_brand",
    ),
    path(
        "save_company/",
        goodbuyDatabase_endpoints.endpoint_save_company,
        name="endpoint_save_company",
    ),
    path(
        "save_corporation/",
        goodbuyDatabase_endpoints.endpoint_save_corporation,
        name="endpoint_save_corporation",
    ),
    path(
        "save_country/",
        goodbuyDatabase_endpoints.endpoint_save_country,
        name="endpoint_save_country",
    ),
    path(
        "current_categories/",
        goodbuyDatabase_endpoints.current_categories,
        name="current_categories",
    ),
    path(
        "product_validation/",
        goodbuyDatabase_endpoints.product_validation,
        name="product_validation",
    ),
]
