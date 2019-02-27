from django.contrib import admin
from .models import Concerns, Companies, Brands, Products
# Register your models here.
class ConcernsAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "id",)
    search_fields = ["name", "rating", "id",]

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "concern", "id",)
    search_fields = ["name", "logo", "concern", "id",]

class BrandsAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "id",)
    search_fields = ["name", "logo", "id",]
    autocomplete_fields = ("concern", "company",)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name",  "ean", "image", "group", "brand", "id",)
    search_fields = ["name", "id",]
    autocomplete_fields = ("brand", "concern",)

admin.site.register(Concerns, ConcernsAdmin)
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)
