from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "countries"
        verbose_name_plural = "Countries"
        ordering = ("name","id",)

    def __str__(self):
        return self.name

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "stores"
        ordering = ("name","id",)

class Corporation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=45,
        verbose_name="Corporation Name",
        unique=True,
        )
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'corporations'
        ordering = ("name","id",)

    def __str__(self):
        return self.name

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    humans = models.IntegerField(
        validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    humans_description = models.TextField(null=True,blank=True,)
    environment = models.IntegerField(validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    environment_description = models.TextField(null=True,blank=True,)
    animals = models.IntegerField(validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    animals_description = models.TextField(null=True,blank=True,)
    corporation = models.OneToOneField(
        Corporation,
        models.SET_NULL,
        null=True,
        blank=True,
        )

    class Meta:
        managed = True
        db_table = "ratings"
        ordering = ("corporation","id",)

    def __str__(self):
        return self.corporation.name

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    corporation = models.ForeignKey(Corporation,
        models.SET_NULL,
        db_column="corporation",
        null=True,
        blank=True
        )
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'companies'
        ordering = ("name","id",)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company, models.SET_NULL, null=True, blank=True)
    corporation = models.ForeignKey(
        Corporation, models.SET_NULL, null=True, blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'brands'
        ordering = ("name","id",)

    def __str__(self):
        return self.name

class CategoryOfProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "category_of_products"
        ordering = ("name","id",)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(unique=True, max_length=45,)
    wiki = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'certificates'
        ordering = ("name","id",)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, verbose_name="Product Name")
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    code = models.CharField(null=True,blank=True,unique=True, max_length=13)
    scraped_image = models.URLField(null=True, blank=True)
    image_of_front = models.ImageField(
        default="default.svg",
        upload_to="product_image",
        null=True,
        blank=True)
    image_of_details = models.ImageField(
        default="default.svg",
        upload_to="product_image",
        null=True,
        blank=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, null=True, blank=True)
    corporation = models.ForeignKey(
        Corporation, models.SET_NULL, null=True, blank=True
        )
    product_category = models.ForeignKey(CategoryOfProduct,
        models.SET_NULL,
        null=True,
        blank=True,
        )
    certificate = models.ManyToManyField(Certificate, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    scanned_counter = models.IntegerField(default=1, null=True, blank=True)
    added_by = models.ForeignKey(
        User,models.SET_NULL, null=True, blank=True, related_name="creator"
        )
    checked = models.BooleanField(null=True)
    checked_by = models.ForeignKey(
        User,models.SET_NULL, null=True, blank=True, related_name="inspector"
        )

    class Meta:
        managed = True
        db_table = 'products'
        ordering = ("name","id",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("goodbuyDatabase:product_list")

    def delete(self, *args, **kwargs):
        # So the default image not get deleted
        if self.image_of_front != "default.svg":
            print("image:",type(self.image_of_front))
            self.image_of_front.delete()
        if self.image_of_details != "default.svg":
            print("image:",type(self.image_of_details))
            self.image_of_details.delete()
        super().delete(*args, **kwargs)

class ProductPriceInStore(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_price_in_store'

    def __str__(self):
        return str(self.price)
