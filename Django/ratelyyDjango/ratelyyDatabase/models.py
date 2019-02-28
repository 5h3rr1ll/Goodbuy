from django.db import models

class Concern(models.Model):
    RATINGS = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,verbose_name="Concern Name",unique=True)
    logo = models.URLField(null=True,blank=True)
    wiki = models.URLField(null=True,blank=True)
    rating = models.CharField(max_length=2, choices=RATINGS,default=0,null=True,blank=True)
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
    logo = models.URLField(null=True,blank=True)
    wiki = models.URLField(null=True,blank=True)
    concern = models.ForeignKey(Concern,models.CASCADE,db_column="concern",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id', 'concern'),)
        ordering = ("name",)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField(null=True,blank=True)
    wiki = models.URLField(null=True,blank=True)
    company = models.ForeignKey(Company,models.CASCADE,null=True,blank=True)
    concern = models.ForeignKey(Concern,models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField(null=True,blank=True)
    wiki = models.URLField(null=True,blank=True)
    gtin = models.PositiveIntegerField(null=True,blank=True,verbose_name="GTIN")
    image = models.URLField(null=True,blank=True)
    group = models.CharField(max_length=45,null=True,blank=True)
    brand = models.ForeignKey(Brand, models.CASCADE)
    concern = models.ForeignKey(Concern, models.CASCADE,null=True,blank=True,default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'products'
        unique_together = (('id','brand'),)

    def __str__(self):
        return self.name
