from django.contrib import admin

from .models import (
    Brand,
    Certificate,
    Company,
    Corporation,
    Country,
    Product,
    ProductPriceInStore,
    Rating,
    Store,
    MainProductCategory,
    ProductCategory,
    SubProductCategory,
)


class MainProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "created",
        "updated",
    )

    search_fields = [
        "name",
    ]


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "created",
        "updated",
    )

    search_fields = [
        "name",
    ]


class SubProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "created",
        "updated",
    )

    search_fields = [
        "name",
    ]


class RatingAdmin(admin.ModelAdmin):
    list_display = ("corporation",)
    list_display_links = ("corporation",)

    @classmethod
    def corporation(self, obj):
        if obj.corporation is not None:
            return obj.corporation.name
        else:
            return None

    corporation.short_description = "Rating of associated Concern"


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
        "code",
        "created",
        "updated",
    ]


class RatingInline(admin.StackedInline):
    max_num = 1
    model = Rating


class CorporationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "wiki",
        "origin",
        "origin_code",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
    ]
    autocomplete_fields = ("origin",)
    inlines = [
        RatingInline,
    ]

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "wiki",
        "corporation",
        "origin",
        "origin_code",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
        "logo",
        "corporation__name",
        "origin",
        "created",
        "updated",
    ]
    autocomplete_fields = ("corporation",)

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "wiki",
        "company",
        "corporation",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
        "logo",
        "wiki",
        "company__name",
        "corporation__name",
        "created",
        "updated",
    ]
    autocomplete_fields = (
        "corporation",
        "company",
    )


class ProdcutPriceInStoreAdmin(admin.ModelAdmin):
    list_display = ("store", "product", "price")
    search_fields = ["store__name", "product__name", "price"]


class PriceInline(admin.StackedInline):
    max_num = 1
    model = ProductPriceInStore


class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "wiki",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
        "created",
        "updated",
    ]
    autocomplete_fields = ("product",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "state",
        "code",
        "brand",
        "checked_by",
        "scanned_counter",
        "data_source",
        "added_by",
        "logo",
        "wiki",
        "scraped_image",
        "created",
        "updated",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
        "code",
        "brand__name",
        "scanned_counter",
        "created",
        "updated",
        "checked_by__username",
    ]
    exclude = ("scanned_counter", "added_by")
    autocomplete_fields = ("brand",)
    inlines = [
        PriceInline,
    ]


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
    )
    list_display_links = ("name",)
    search_fields = [
        "name",
    ]
    autocomplete_fields = ()


admin.site.site_header = "Goodbuy Database"
admin.site.register(
    Corporation, CorporationAdmin,
)
admin.site.register(
    Company, CompanyAdmin,
)
admin.site.register(
    Brand, BrandAdmin,
)
admin.site.register(
    Product, ProductAdmin,
)
admin.site.register(
    Country, CountryAdmin,
)
admin.site.register(
    Rating, RatingAdmin,
)
admin.site.register(
    MainProductCategory, MainProductCategoryAdmin,
)
admin.site.register(
    ProductCategory, ProductCategoryAdmin,
)
admin.site.register(
    SubProductCategory, SubProductCategoryAdmin,
)
admin.site.register(
    Store, StoreAdmin,
)
admin.site.register(
    ProductPriceInStore, ProdcutPriceInStoreAdmin,
)
admin.site.register(
    Certificate, CertificateAdmin,
)
