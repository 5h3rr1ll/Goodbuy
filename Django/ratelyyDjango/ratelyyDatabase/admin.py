from django.contrib import admin
from .models import ConcernsOld, CompaniesOld, BrandsOld, ProductsOld, Concerns, Companies, Brands, Products

# Register your models here.
class ConcernsAdmin(admin.ModelAdmin):
    list_display = ("id_concern", "concern_name",)
    search_fields = ["id_concern", "concern_name"]

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("id_company", "company_name",)
    search_fields = ["id_company", "company_name"]

class BrandsAdmin(admin.ModelAdmin):
    list_display = ("id_brand", "brand_name",)
    search_fields = ["id_brand", "brand_name"]

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id_product", "product_name",)
    search_fields = ["id_product", "product_name"]


class ConcernsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


class CompaniesOldAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


class BrandsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]

class ProductsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Concerns, ConcernsAdmin)
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)

admin.site.register(ConcernsOld, ConcernsOldAdmin)
admin.site.register(CompaniesOld, CompaniesOldAdmin)
admin.site.register(BrandsOld, BrandsOldAdmin)
admin.site.register(ProductsOld, ProductsOldAdmin)
