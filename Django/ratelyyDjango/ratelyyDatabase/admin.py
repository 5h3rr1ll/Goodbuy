from django.contrib import admin
from .models import Concern, Company, Brand, Product, Country
# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "created", "updated")
    list_display_links = ("id", "name")
    search_field = ["id", "name", "code", "created", "updated"]

class ConcernAdmin(admin.ModelAdmin):
    list_display = ("id","name","logo","wiki","rating","origin_code","created","updated",)
    list_display_links = ("id","name")
    search_fields = ["id","name","logo","wiki","rating","origin_code","created","updated",]

    def origin_code(self, obj):
        if obj.origin is not None:
            return obj.origin.code
        else:
            return None

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","name","logo","wiki","concern","concern_rating","origin_code","created","updated",)
    list_display_links = ("id","name")
    search_fields = ["id","name", "logo", "concern","concern_rating","origin_code","created","updated",]
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
    list_display = ("id","name", "logo", "wiki", "company","concern","concern_rating","created", "updated",)
    list_display_links = ("id","name")
    search_fields = ["id","name", "logo", "wiki", "company","concern","concern_rating","created", "updated",]
    autocomplete_fields = ("concern", "company",)

    def concern_rating(self, obj):
        if obj.concern is not None:
            return obj.concern.rating
        else:
            return None
    concern_rating.short_description = "Rating of associated Concern"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name",  "logo", "wiki", "gtin", "image", "group", "brand", "concern","concern_rating","created", "updated",)
    list_display_links = ("id","name")
    search_fields = ["id","name",  "logo", "wiki", "gtin", "image", "group", "brand", "concern","concern_rating","created", "updated",]
    autocomplete_fields = ("brand", "concern",)

    def concern_rating(self, obj):
        if obj.concern is not None:
            return obj.concern.rating
        else:
            return None
    concern_rating.short_description = "Rating of associated Concern"
    concern_rating.admin_order_field = "rating"

admin.site.register(Concern, ConcernAdmin,)
admin.site.register(Company, CompanyAdmin,)
admin.site.register(Brand, BrandAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Country, CountryAdmin,)
admin.site.site_header = "Goodbuy Database"
