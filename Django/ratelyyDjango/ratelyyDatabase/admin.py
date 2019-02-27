from django.contrib import admin
from .models import Concern, Company, Brand, Product
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
    list_display = ("id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern","concern_rating","created", "updated",)
    search_fields = ["id","name",  "logo", "wiki", "ean", "image", "group", "brand", "concern","concern_rating","created", "updated",]
    autocomplete_fields = ("brand", "concern",)

    def concern_rating(self, obj):
        return obj.concern.rating

admin.site.register(Concern, ConcernAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
