from django.contrib import admin
from .models import (
    Concern, Company, Brand,
    Product, Country, Rating,
    Store, ProductPriceInStore,
    MainCategoryOfProduct, SubCategoryOfProduct,
    )
# Register your models here.
class MainCategoryOfProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "updated",)
    list_display_links = ("id", "name", "created", "updated",)

class SubCategoryOfProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "updated",)
    list_display_links = ("id", "name", "created", "updated",)

class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)

class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "created", "updated",)
    list_display_links = ("id", "name",)
    search_field = ["id", "name", "code", "created", "updated",]

class ConcernAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki", "rating",
        "origin_code", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "rating",
        "origin_code", "created", "updated",
        ]

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None

class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki", "concern",
        "concern_rating", "origin_code", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "concern", "concern_rating",
        "origin_code", "created", "updated",
        ]
    autocomplete_fields = ("concern",)

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None

    def concern_rating(self, obj):
        if obj.concern is not None:
            return obj.concern.rating
        else:
            return None
    concern_rating.short_description = "Rating of associated Concern"

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "logo", "wiki", "company",
        "concern", "concern_rating", "created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "company",
        "concern", "concern_rating", "created", "updated",
        ]
    autocomplete_fields = ("concern", "company",)

    def concern_rating(self, obj):
        if obj.concern is not None:
            return obj.concern.rating
        else:
            return None
    concern_rating.short_description = "Rating of associated Concern"

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
        "id", "name", "logo", "wiki", "gtin",
        "image", "brand", "concern",
        "concern_rating", "stat_counter" ,"created", "updated",
        )
    list_display_links = ("id", "name")
    search_fields = [
        "id", "name", "logo", "wiki", "gtin",
        "image", "brand", "concern",
        "concern_rating", "stat_counter" ,"created", "updated",
        ]
    exclude = ("stat_counter",)

    autocomplete_fields = ("brand", "concern",)

    def concern_rating(self, obj):
        if obj.concern is not None:
            return obj.concern.rating
        else:
            return None
    concern_rating.short_description = "Rating of associated Concern"
    concern_rating.admin_order_field = "rating"

    inlines = [
        PriceInline,
    ]
class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country",)
    search_fields = [
        "id", "name",
    ]
    autocomplete_fields = ()

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
