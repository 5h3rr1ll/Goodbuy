from django.contrib import admin

from .models import (Brand, Certificate, Company, Corporation, Country,
                     Product, ProductPriceInStore, Rating, Store,
                     CategoryOfProduct, SubCategoryOfProduct)


class CategoryOfProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created",
        "updated",
    )
    list_display_links = (
        "id",
        "name",
        "created",
        "updated",
    )


class SubCategoryOfProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "main_category",
        "created",
        "updated",
    )
    list_display_links = (
        "id",
        "name",
        "created",
        "updated",
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "corporation",
    )
    list_display_links = (
        "id",
        "corporation",
    )

    @classmethod
    def corporation(self, obj):
        if obj.corporation is not None:
            return obj.corporation.name
        else:
            return None

    corporation.short_description = "Rating of associated Concern"


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "code",
        "created",
        "updated",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = [
        "id",
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
        "id",
        "name",
        "logo",
        "wiki",
        "origin",
        "origin_code",
        "created",
        "updated",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "name",
        "id",
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
        "id",
        "name",
        "logo",
        "wiki",
        "corporation",
        "origin",
        "origin_code",
        "created",
        "updated",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "id",
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
        "id",
        "name",
        "logo",
        "wiki",
        "company",
        "corporation",
        "created",
        "updated",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "id",
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
    list_display = ("id", "store", "product", "price")
    search_fields = ["id", "store__name", "product__name", "price"]


class PriceInline(admin.StackedInline):
    max_num = 1
    model = ProductPriceInStore


class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "wiki",
        "created",
        "updated",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "id",
        "name",
        "created",
        "updated",
    ]
    autocomplete_fields = ("product",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "added_by",
        "checked",
        "checked_by",
        "logo",
        "wiki",
        "code",
        "scraped_image",
        "brand",
        "scanned_counter",
        "created",
        "updated",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "id",
        "name",
        "code",
        "brand__name",
        "scanned_counter",
        "created",
        "updated",
        "checked_by__name",
    ]
    exclude = ("scanned_counter", "added_by")
    autocomplete_fields = (
        "brand",
    )
    inlines = [
        PriceInline,
    ]


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
    )
    list_display_links = ("id", "name")
    search_fields = [
        "id",
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
    CategoryOfProduct, CategoryOfProductAdmin,
)
admin.site.register(
    SubCategoryOfProduct, SubCategoryOfProductAdmin,
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
