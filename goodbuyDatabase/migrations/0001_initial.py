# Generated by Django 2.2.5 on 2019-12-23 20:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'brands',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('name', models.CharField(db_index=True, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'certificates',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('name', models.CharField(db_index=True, max_length=45, primary_key=True, serialize=False, unique=True, verbose_name='Corporation Name')),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'corporations',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(blank=True, db_index=True, max_length=8, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MainProductCategory',
            fields=[
                ('name', models.CharField(db_index=True, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'main_category_of_products',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Product Name')),
                ('code', models.CharField(blank=True, db_index=True, max_length=13, null=True, unique=True)),
                ('scanned_counter', models.IntegerField(blank=True, db_index=True, default=1, null=True, verbose_name='Scanned Counter')),
                ('state', models.CharField(choices=[('200', 'checked'), ('209', 'pending'), ('306', 'incomplete'), ('211', 'unchecked')], db_index=True, max_length=10)),
                ('data_source', models.CharField(choices=[('1', 'OFF'), ('2', 'CC'), ('3', 'User')], db_index=True, max_length=5, verbose_name='Data Source')),
                ('scraped_image', models.URLField(blank=True, null=True, verbose_name='Scraped Image')),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('image_of_front', models.ImageField(blank=True, default='default.svg', null=True, upload_to='product_image', verbose_name='Image of Front')),
                ('image_of_details', models.ImageField(blank=True, default='default.svg', null=True, upload_to='product_image', verbose_name='Image of Details')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Brand')),
                ('certificate', models.ManyToManyField(blank=True, to='goodbuyDatabase.Certificate')),
                ('checked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspector', to=settings.AUTH_USER_MODEL)),
                ('main_product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.MainProductCategory', verbose_name='Main Product Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('name', models.CharField(db_index=True, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.MainProductCategory')),
            ],
            options={
                'db_table': 'category_of_products',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubProductCategory',
            fields=[
                ('name', models.CharField(db_index=True, max_length=45, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category_of_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.ProductCategory')),
            ],
            options={
                'db_table': 'sub_category_of_products',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('name', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Country')),
            ],
            options={
                'db_table': 'stores',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, db_index=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(9999)])),
                ('land_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('land_rating_text', models.TextField(blank=True, null=True)),
                ('land_definition', models.URLField(blank=True, null=True)),
                ('women_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('women_rating_text', models.TextField(blank=True, null=True)),
                ('women_definition', models.URLField(blank=True, null=True)),
                ('farmers_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('farmers_rating_text', models.TextField(blank=True, null=True)),
                ('farmers_definition', models.URLField(blank=True, null=True)),
                ('workers_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('workers_rating_text', models.TextField(blank=True, null=True)),
                ('workers_definition', models.URLField(blank=True, null=True)),
                ('climate_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('climate_rating_text', models.TextField(blank=True, null=True)),
                ('climate_definition', models.URLField(blank=True, null=True)),
                ('transparency_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('transparency_rating_text', models.TextField(blank=True, null=True)),
                ('transparency_definition', models.URLField(blank=True, null=True)),
                ('water_value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('water_rating_text', models.TextField(blank=True, null=True)),
                ('water_definition', models.URLField(blank=True, null=True)),
                ('corporation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Corporation')),
            ],
            options={
                'db_table': 'ratings',
                'ordering': ('corporation',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductPriceInStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodbuyDatabase.Product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodbuyDatabase.Store')),
            ],
            options={
                'db_table': 'product_price_in_store',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.ProductCategory', verbose_name='Product Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.SubProductCategory', verbose_name='Sub Product Category'),
        ),
        migrations.AddField(
            model_name='corporation',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Country'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('corporation', models.ForeignKey(blank=True, db_column='corporation', null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Corporation')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Country')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Company'),
        ),
        migrations.AddField(
            model_name='brand',
            name='corporation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Corporation'),
        ),
    ]
