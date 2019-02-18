from django.db import models

class Concerns(models.Model):
    id_concern = models.IntegerField(primary_key=True)
    concern_name = models.CharField(max_length=45)
    RATINGS = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    concern_rating = models.CharField(max_length=2, choices=RATINGS)    

    class Meta:
            managed = True
            db_table = 'concerns'
            # this do the trick that django admin doesn't place a further s after
            # the table name. Source: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
            verbose_name_plural = "concerns"

class Companies(models.Model):
    id_company = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=45)
    company_logo = models.CharField(max_length=45, blank=True, null=True)
    concerns_id_concern = models.ForeignKey('Concerns', models.DO_NOTHING, db_column='concerns_id_concern')

    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id_company', 'concerns_id_concern'),)
        verbose_name_plural = "companies"


class Brands(models.Model):
    id_brand = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=45)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brands'
        verbose_name_plural = "brands"

class Products(models.Model):
    id_product = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=45)
    product_ean = models.CharField(max_length=45, blank=True, null=True)
    product_image = models.CharField(max_length=45, blank=True, null=True)
    product_group = models.CharField(max_length=200, blank=True, null=True)
    brands_id_brand = models.ForeignKey(Brands, models.DO_NOTHING, db_column='brands_id_brand')

    class Meta:
        managed = True
        db_table = 'products'
        unique_together = (('id_product', 'brands_id_brand'),)
        verbose_name_plural = "products"


class ConcernsOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'concerns_old'

class CompaniesOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'companies_old'

class BrandsOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brands_old'

class ProductsOld(models.Model):
    name = models.CharField(max_length=50)
    ean = models.IntegerField()
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products_old'
