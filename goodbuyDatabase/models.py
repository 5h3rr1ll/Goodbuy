from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=50, db_index=True
    )
    code = models.CharField(
        unique=False, max_length=8, null=True, blank=True, db_index=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "countries"
        verbose_name_plural = "Countries"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=50, db_index=True
    )
    country = models.ForeignKey(
        Country, models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "stores"
        ordering = ("name",)


class Corporation(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=45,
        verbose_name="Corporation Name",
        unique=True,
        db_index=True,
    )
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "corporations"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Rating(models.Model):
    corporation = models.ForeignKey(
        Corporation, models.SET_NULL, null=True, blank=False
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)],
        null=True,
        blank=True,
        db_index=True,
    )
    land_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    land_rating_text = models.TextField(null=True, blank=True,)
    land_definition = models.URLField(null=True, blank=True)
    women_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    women_rating_text = models.TextField(null=True, blank=True,)
    women_definition = models.URLField(null=True, blank=True)
    farmers_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    farmers_rating_text = models.TextField(null=True, blank=True,)
    farmers_definition = models.URLField(null=True, blank=True)
    workers_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    workers_rating_text = models.TextField(null=True, blank=True,)
    workers_definition = models.URLField(null=True, blank=True)
    climate_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    climate_rating_text = models.TextField(null=True, blank=True,)
    climate_definition = models.URLField(null=True, blank=True)
    transparency_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    transparency_rating_text = models.TextField(null=True, blank=True,)
    transparency_definition = models.URLField(null=True, blank=True)
    water_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
    )
    water_rating_text = models.TextField(null=True, blank=True,)
    water_definition = models.URLField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = "ratings"
        ordering = ("corporation",)

    def __str__(self):
        return self.year, self.corporation.name


class Company(models.Model):
    name = models.CharField(
        primary_key=True, max_length=50, unique=True, db_index=True
    )
    corporation = models.ForeignKey(
        Corporation,
        models.SET_NULL,
        db_column="corporation",
        null=True,
        blank=True,
    )
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "companies"
        ordering = ("name",)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(unique=False, max_length=100, db_index=True)
    company = models.ForeignKey(
        Company, models.SET_NULL, null=True, blank=True
    )
    corporation = models.ForeignKey(
        Corporation, models.SET_NULL, null=True, blank=True
    )
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "brands"
        ordering = ("name",)

    def __str__(self):
        return self.name


class MainProductCategory(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=45, db_index=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "main_category_of_products"
        ordering = ("name",)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=45, db_index=True
    )
    main_category = models.ForeignKey(
        MainProductCategory, models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "category_of_products"
        ordering = ("name",)

    def __str__(self):
        return self.name


class SubProductCategory(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=45, db_index=True
    )
    category_of_product = models.ForeignKey(
        ProductCategory, models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "sub_category_of_products"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=45, db_index=True
    )
    wiki = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "certificates"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATE = (
        ("200", "checked"),
        ("209", "pending"),
        ("306", "incomplete"),
        ("211", "unchecked"),
    )
    SOURCE = [
        ("1", "OFF"),
        ("2", "CC"),
        ("3", "User"),
    ]
    name = models.CharField(
        max_length=100,
        verbose_name="Product Name",
        null=True,
        blank=True,
        db_index=True,
    )
    code = models.CharField(
        null=True, blank=True, unique=True, max_length=13, db_index=True
    )
    scanned_counter = models.IntegerField(
        default=1,
        verbose_name="Scanned Counter",
        null=True,
        blank=True,
        db_index=True,
    )
    upvote_counter = models.IntegerField(
        default=0,
        verbose_name="Upvote Counter",
        null=True,
        blank=True,
        db_index=True,
    )
    downvote_counter = models.IntegerField(
        default=0,
        verbose_name="Downvote Counter",
        null=True,
        blank=True,
        db_index=True,
    )
    added_by = models.ForeignKey(
        User, models.SET_NULL, null=True, blank=True, related_name="creator"
    )
    state = models.CharField(max_length=10, choices=STATE, db_index=True)
    checked_by = models.ForeignKey(
        User, models.SET_NULL, null=True, blank=True, related_name="inspector"
    )
    brand = models.ForeignKey(Brand, models.SET_NULL, null=True, blank=True)
    main_product_category = models.ForeignKey(
        MainProductCategory,
        models.SET_NULL,
        verbose_name="Main Product Category",
        null=True,
        blank=True,
    )
    product_category = models.ForeignKey(
        ProductCategory,
        models.SET_NULL,
        verbose_name="Product Category",
        null=True,
        blank=True,
    )
    sub_product_category = models.ForeignKey(
        SubProductCategory,
        models.SET_NULL,
        verbose_name="Sub Product Category",
        null=True,
        blank=True,
    )
    data_source = models.CharField(
        max_length=5, verbose_name="Data Source", choices=SOURCE, db_index=True
    )
    scraped_image = models.URLField(
        verbose_name="Scraped Image", null=True, blank=True
    )
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    image_of_front = models.ImageField(
        default="default.svg",
        upload_to="product_image",
        verbose_name="Image of Front",
        null=True,
        blank=True,
    )
    image_of_details = models.ImageField(
        default="default.svg",
        upload_to="product_image",
        verbose_name="Image of Details",
        null=True,
        blank=True,
    )
    certificate = models.ManyToManyField(Certificate, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "products"
        ordering = ("name",)

    def __str__(self):
        if self.name:
            return self.name
        return self.code

    def get_absolute_url(self):
        return reverse("goodbuyDatabase:product_list")

    def delete(self, *args, **kwargs):
        # So the default image not get deleted
        if self.image_of_front != "default.svg":
            print("image:", type(self.image_of_front))
            self.image_of_front.delete()
        if self.image_of_details != "default.svg":
            print("image:", type(self.image_of_details))
            self.image_of_details.delete()
        super().delete(*args, **kwargs)


class ProductPriceInStore(models.Model):
    store = models.ForeignKey(Store, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "product_price_in_store"

    def __str__(self):
        return str(self.price)


class BigTen(models.Model):
    name = models.CharField(
        primary_key=True, unique=True, max_length=45, db_index=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "big_ten"
        verbose_name_plural = "Big Ten"

    def __str__(self):
        return str(self.name)
