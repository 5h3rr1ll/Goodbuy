from django.contrib import admin
from .models import Concerns, Companies, Brands, Products
# Register your models here.
class ConcernAdmin(admin.ModelAdmin):
    list_display = ("id","name","logo","wiki","rating","created","updated",)
    search_fields = ["id","name","logo","wiki","rating","created","updated",]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","name","logo","wiki","concern","created","updated",)
    search_fields = ["id","name", "logo", "concern","created","updated",]

class BrandAdmin(admin.ModelAdmin):
    list_display = ("id","name", "logo", "wiki", "company","concern","created", "updated",)
    search_fields = ["id","name", "logo", "wiki", "company","concern","created", "updated",]
    autocomplete_fields = ("concern", "company",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern","created", "updated",)
    search_fields = ["id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern","created", "updated",]
    autocomplete_fields = ("brand", "concern",)

admin.site.register(Concerns, ConcernAdmin)
admin.site.register(Companies, CompanyAdmin)
admin.site.register(Brands, BrandAdmin)
admin.site.register(Products, ProductAdmin)
