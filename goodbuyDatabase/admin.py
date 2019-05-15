from django.contrib import admin
from .models import (
    Corporation, Company, Brand,
    Product, Country, Rating,
    Store, ProductPriceInStore,
    MainCategoryOfProduct, SubCategoryOfProduct,
    Certificate,
    )
# Register your models here.
class MainCategoryOfProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "updated",)
    list_display_links = ("id", "name", "created", "updated",)

class SubCategoryOfProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "updated",)
    list_display_links = ("id", "name", "created", "updated",)

class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "corporation" , "humans", "environment", "animals",
     "animals_description", "environment_description", "humans_description")
    list_display_links = ("id", "corporation",  "humans", "environment", "animals")

    @classmethod
    def corporation(self, obj):
        if obj.corporation is not None:
            return obj.corporation.name
        else:
            return None
    corporation.short_description = "Rating of associated Concern"

class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "created", "updated",)
    list_display_links = ("id", "name",)
    search_fields = ["id", "name", "code", "created", "updated",]

class RatingInline(admin.StackedInline):
    max_num = 1
    model = Rating

class CorporationAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki",
        "origin_code", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki",
        "origin_code", "created", "updated",
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
        "id", "name", "logo", "wiki", "corporation",
        "origin_code", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "corporation__name",
        "origin_code", "created", "updated",
        ]
    autocomplete_fields = ("corporation",)

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki", "company",
        "corporation", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "company__name",
        "corporation__name", "created", "updated",
        ]
    autocomplete_fields = ("corporation", "company",)

class ProdcutPriceInStoreAdmin(admin.ModelAdmin):
    list_display = ("id","store","product","price")
    search_fields = [
        "id","store__name","product__name","price"
    ]

class PriceInline(admin.StackedInline):
    max_num = 1
    model = ProductPriceInStore

class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "wiki", "created", "updated",)
    list_display_links = ("id", "name")
    search_fields = ["id", "name", "created", "updated",]
    autocomplete_fields = ("product",)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name","added_by", "logo", "wiki", "code",
        "image", "brand", "corporation",
        "scanned_counter" ,"created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "code",
        "image", "brand__name", "corporation__name",
        "scanned_counter" ,"created", "updated",
        ]
    exclude = ("scanned_counter","added_by")
    autocomplete_fields = ("brand", "corporation",)
    inlines = [ PriceInline, ]

class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country",)
    search_fields = [
        "id", "name",
    ]
    autocomplete_fields = ()

admin.site.site_header = "Goodbuy Database"
admin.site.register(Corporation, CorporationAdmin,)
admin.site.register(Company, CompanyAdmin,)
admin.site.register(Brand, BrandAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Country, CountryAdmin,)
admin.site.register(Rating, RatingAdmin,)
admin.site.register(MainCategoryOfProduct, MainCategoryOfProductAdmin,)
admin.site.register(SubCategoryOfProduct, SubCategoryOfProductAdmin,)
admin.site.register(Store, StoreAdmin,)
admin.site.register(ProductPriceInStore, ProdcutPriceInStoreAdmin,)
admin.site.register(Certificate,CertificateAdmin,)
