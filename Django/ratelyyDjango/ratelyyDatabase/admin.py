from django.contrib import admin
from .models import ConcernsOld, CompaniesOld, BrandsOld, ProductsOld, Concerns

# Register your models here.

class ConcernsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)

class CompaniesOldAdmin(admin.ModelAdmin):
    list_display = ("name",)

class BrandsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ProductsOldAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ConcernsAdmin(admin.ModelAdmin):
    list_display = ("id_concern", "concern_name",)

admin.site.register(ConcernsOld, ConcernsOldAdmin)
admin.site.register(CompaniesOld, CompaniesOldAdmin)
admin.site.register(BrandsOld, BrandsOldAdmin)
admin.site.register(ProductsOld, ProductsOldAdmin)
admin.site.register(Concerns, ConcernsAdmin)
