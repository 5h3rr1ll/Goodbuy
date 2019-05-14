from django.contrib import admin
from .models import (
    Concern, Company, Brand,
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
    list_display = ("id", "concern" , "humans", "environment", "animals",
     "animals_description", "environment_description", "humans_description")
    list_display_links = ("id", "concern",  "humans", "environment", "animals")

    @classmethod
    def concern(self, obj):
        if obj.concern is not None:
            return obj.concern.name
        else:
            return None
    concern.short_description = "Rating of associated Concern"

class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "created", "updated",)
    list_display_links = ("id", "name",)
    search_fields = ["id", "name", "code", "created", "updated",]

class RatingInline(admin.StackedInline):
    max_num = 1
    model = Rating

class ConcernAdmin(admin.ModelAdmin):
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
        "id", "name", "logo", "wiki", "concern",
        "origin_code", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "concern__name",
        "origin_code", "created", "updated",
        ]
    autocomplete_fields = ("concern",)

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki", "company",
        "concern", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "company__name",
        "concern__name", "created", "updated",
        ]
    autocomplete_fields = ("concern", "company",)

class ProdcutPriceInStoreAdmin(admin.ModelAdmin):
    list_display = ("id","store","product","price")
    search_fields = [
        "id","store__name","product__name","price"
    ]

class PriceInline(admin.StackedInline):
    max_num = 1
    model = ProductPriceInStore

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name","added_by", "logo", "wiki", "code",
        "image", "brand", "concern",
        "scanned_counter" ,"created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "code",
        "image", "brand__name", "concern__name",
        "scanned_counter" ,"created", "updated",
        ]
    exclude = ()
    autocomplete_fields = ("brand", "concern",)
    inlines = [
        PriceInline,
    ]

class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country",)
    search_fields = [
        "id", "name",
    ]
    autocomplete_fields = ()

class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "wiki", "created", "updated",)
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "product__name", "created", "updated",]
    autocomplete_fields = ("product",)

admin.site.site_header = "Goodbuy Database"
admin.site.register(Concern, ConcernAdmin,)
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
