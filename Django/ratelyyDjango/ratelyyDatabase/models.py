from django.db import models

class Concerns(models.Model):
    id_concern = models.IntegerField(primary_key=True)
    concern_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'concerns'
        verbose_name_plural = "concerns"

class ConcernsOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'concerns_old'

class CompaniesOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies_old'

class BrandsOld(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands_old'

class ProductsOld(models.Model):
    name = models.CharField(max_length=50)
    ean = models.IntegerField()
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_old'
