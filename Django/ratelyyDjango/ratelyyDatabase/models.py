from django.db import models

class Concern(models.Model):
    ratings = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,verbose_name="Concern Name",unique=True)
    logo = models.URLField()
    wiki = models.URLField()
    rating = models.CharField(max_length=2, choices=ratings,default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
            managed = True
            db_table = 'concerns'
            # this do the trick that django admin doesn't place a further s after
            # the table name. Source: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
            ordering = ("name",)

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,unique=True)
    logo = models.URLField()
    wiki = models.URLField()
    concern = models.ForeignKey(Concerns,models.CASCADE,db_column="concern",related_name="companies")
    concern_rating = models.ForeignKey(Concerns,models.CASCADE,related_name="companies_rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
       return self.concern.rating


    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id', 'concern'),)
        ordering = ("name",)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField()
    wiki = models.URLField()
    company = models.ForeignKey(Companies, models.CASCADE)
    concern = models.ForeignKey(Concerns, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'brands'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField()
    wiki = models.URLField()
    ean = models.CharField(max_length=45,verbose_name="EAN")
    image = models.CharField(max_length=45,)
    group = models.CharField(max_length=200,)
    brand = models.ForeignKey(Brands, models.CASCADE)
    concern = models.ForeignKey(Concerns, models.CASCADE,related_name="products")
    concern_rating = models.ForeignKey(Concerns,models.CASCADE,related_name="products_rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
       return self.concerns.rating

    class Meta:
        managed = False
        db_table = 'products'
        unique_together = (('id','brand'),)
