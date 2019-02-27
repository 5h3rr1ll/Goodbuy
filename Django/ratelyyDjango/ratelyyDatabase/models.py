from django.db import models

class Concern(models.Model):
    RATINGS = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,verbose_name="Concern Name",unique=True)
    logo = models.URLField()
    wiki = models.URLField()
    rating = models.CharField(max_length=2, choices=RATINGS,default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            managed = True
            db_table = 'concerns'
            ordering = ("name",)

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,unique=True)
    logo = models.URLField()
    wiki = models.URLField()
    concern = models.ForeignKey(Concern,models.CASCADE,db_column="concern",related_name="companies")
    concern_rating = models.ForeignKey(Concern,models.CASCADE,related_name="companies_rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id', 'concern'),)
        ordering = ("name",)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField()
    wiki = models.URLField()
    company = models.ForeignKey(Company, models.CASCADE)
    concern = models.ForeignKey(Concern, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField()
    wiki = models.URLField()
    ean = models.CharField(max_length=45,verbose_name="EAN")
    image = models.CharField(max_length=45,)
    group = models.CharField(max_length=200,)
    brand = models.ForeignKey(Brand, models.CASCADE)
    concern = models.ForeignKey(Concern, models.CASCADE,related_name="products")
    concern_rating = models.ForeignKey(Concern,models.CASCADE,related_name="products_rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'products'
        unique_together = (('id','brand'),)

    def __str__(self):
        return self.name
