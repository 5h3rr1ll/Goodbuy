from django.contrib import admin
from .models import Concerns, Companies, Brands, Products
# Register your models here.
class ConcernsAdmin(admin.ModelAdmin):
    list_display = ( "id","name","rating","created","updated",)
    search_fields = ["id","name","rating","created","updated",]

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("id","name","concern_rating", "logo", "concern","created","updated",)
    search_fields = ["id","name","concern_rating", "logo", "concern","created","updated",]

class BrandsAdmin(admin.ModelAdmin):
    list_display = ("name","concern_rating", "logo", "id",)
    search_fields = ["name","concern_rating", "logo", "id",]
    autocomplete_fields = ("concern", "company",)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name","concern_rating",  "ean", "image", "group", "brand", "id",)
    search_fields = ["name","concern_rating",  "ean", "image", "group", "brand", "id",]
    autocomplete_fields = ("brand", "concern",)

admin.site.register(Concerns, ConcernsAdmin)
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)
