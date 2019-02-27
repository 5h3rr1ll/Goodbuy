from django.contrib import admin
from .models import ConcernsOld, CompaniesOld, BrandsOld, ProductsOld, Concerns, Companies, Brands, Products 
# Register your models here.
class ConcernsAdmin(admin.ModelAdmin):
    list_display = ("concern_name", "concern_rating", "id_concern",)
    search_fields = ["concern_name", "concern_rating", "id_concern",]

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_logo", "concerns_id_concern", "id_company",)
    search_fields = ["company_name", "company_logo", "concerns_id_concern", "id_company",]

class BrandsAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "brand_logo", "id_brand",)
    search_fields = ["brand_name", "brand_logo", "id_brand",]
    autocomplete_fields = ("brand_concern",)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_name",  "product_ean", "product_image", "product_group", "brands_id_brand", "id_product",)
    search_fields = ["product_name", "id_product",]






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
