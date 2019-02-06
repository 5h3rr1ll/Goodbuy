from django.contrib import admin
from .models import Concerns
from .models import Products
from .models import Brands
from .models import Companies
# Register your models here.

admin.site.register(Concerns)
admin.site.register(Products)
admin.site.register(Brands)
admin.site.register(Companies)
