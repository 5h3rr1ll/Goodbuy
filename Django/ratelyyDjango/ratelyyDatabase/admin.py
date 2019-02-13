from django.contrib import admin
from .models import ConcernsOld, CompaniesOld, BrandsOld, ProductsOld

# Register your models here.

admin.site.register(ConcernsOld)
admin.site.register(CompaniesOld)
admin.site.register(BrandsOld)
admin.site.register(ProductsOld)
