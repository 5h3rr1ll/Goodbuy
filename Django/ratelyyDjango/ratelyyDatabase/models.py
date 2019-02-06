# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brands'


class Companies(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Companies'


class Concerns(models.Model):
    name = models.CharField(max_length=50)
    fair = models.IntegerField()
    eco = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Concerns'


class Products(models.Model):
    name = models.CharField(max_length=50)
    ean = models.IntegerField()
    fair = models.IntegerField()
    eco = models.IntegerField()
    concern_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Brands(models.Model):
    id_brand = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=45)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class Companies(models.Model):
    id_company = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=45)
    company_logo = models.CharField(max_length=45, blank=True, null=True)
    concerns_id_concern = models.ForeignKey(Concerns, models.DO_NOTHING, db_column='concerns_id_concern')

    class Meta:
        managed = False
        db_table = 'companies'
        unique_together = (('id_company', 'concerns_id_concern'),)


class CompaniesHasBrands(models.Model):
    companies_id_company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='companies_id_company', primary_key=True)
    companies_concerns_id_concern = models.ForeignKey(Companies, models.DO_NOTHING, db_column='companies_concerns_id_concern')
    brands_id_brand = models.ForeignKey(Brands, models.DO_NOTHING, db_column='brands_id_brand')

    class Meta:
        managed = False
        db_table = 'companies_has_brands'
        unique_together = (('companies_id_company', 'companies_concerns_id_concern', 'brands_id_brand'),)


class Concerns(models.Model):
    id_concern = models.IntegerField(primary_key=True)
    concern_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'concerns'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Products(models.Model):
    id_product = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=45)
    product_ean = models.CharField(max_length=45, blank=True, null=True)
    product_image = models.CharField(max_length=45, blank=True, null=True)
    product_group = models.CharField(max_length=200, blank=True, null=True)
    brands_id_brand = models.ForeignKey(Brands, models.DO_NOTHING, db_column='brands_id_brand')

    class Meta:
        managed = False
        db_table = 'products'
        unique_together = (('id_product', 'brands_id_brand'),)
