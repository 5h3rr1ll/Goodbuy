from django.db import models

class Concerns(models.Model):
    id_concern = models.AutoField(primary_key=True)
    concern_name = models.CharField(max_length=45,verbose_name="Concern Name",unique=True)
    ratings = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    concern_rating = models.CharField(max_length=2, choices=ratings,default=0,verbose_name="Concern Rating")
    concern_created = models.DateTimeField(auto_now_add=True)
    concern_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.concern_name

    class Meta:
            managed = True
            db_table = 'concerns'
            # this do the trick that django admin doesn't place a further s after
            # the table name. Source: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
            verbose_name_plural = "concerns"
            ordering = ("concern_name",)

class Companies(models.Model):
    id_company = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=45,unique=True,verbose_name="Company Name")
    company_logo = models.CharField(max_length=45, blank=True, null=True,verbose_name="Company Logo")
    concerns_id_concern = models.ForeignKey('Concerns', models.DO_NOTHING, db_column='concerns_id_concern',verbose_name="Concern")
    company_created = models.DateTimeField(auto_now_add=True)
    company_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id_company', 'concerns_id_concern'),)
        verbose_name_plural = "companies"
        ordering = ("company_name",)


class Brands(models.Model):
    id_brand = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=45,verbose_name="Brand Name")#,unique=True
    brand_logo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Brand Logo")
    companies = models.ManyToManyField(Companies,verbose_name="Company")
    brand_created = models.DateTimeField(auto_now_add=True)
    brand_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.company_name

    def __str__(self):
        return self.brand_name

    class Meta:
        managed = True
        db_table = 'brands'
        verbose_name_plural = "brands"
        ordering = ("brand_name",)

class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45,unique=True)
    product_ean = models.CharField(max_length=45, blank=True, null=True)
    product_image = models.CharField(max_length=45, blank=True, null=True)
    product_group = models.CharField(max_length=200, blank=True, null=True)
    brands_id_brand = models.ForeignKey(Brands, models.CASCADE, db_column='brands_id_brand',verbose_name="Brand")
    product_created = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now=True)

    #with this function the name of the brand becomes returned instead of Object(1),
    #Object(2) etc
    def __unicode__(self):
        return self.brand_name

    def __str__(self):
        return self.product_name

    class Meta:
        managed = True
        db_table = 'products'
        unique_together = (('id_product', 'brands_id_brand'),)
        verbose_name_plural = "products"
        ordering = ("product_name",)


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
