from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'brands',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('origin', models.CharField(blank=True, max_length=56, null=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Concern',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Concern Name')),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, choices=[('Ethical', 'Ethical'), ('Unethical', 'Unethical')], max_length=45, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'concerns',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MainCategoryOfProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'main_category_of_products',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('gtin', models.PositiveIntegerField(blank=True, null=True, verbose_name='GTIN')),
                ('image', models.URLField(blank=True, null=True)),
                ('group', models.CharField(blank=True, max_length=45, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Brand')),
                ('concern', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Concern')),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.MainCategoryOfProduct')),
            ],
            options={
                'db_table': 'products',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategoryOfProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodbuyDatabase.MainCategoryOfProduct')),
            ],
            options={
                'db_table': 'sub_category_of_products',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.SubCategoryOfProduct'),
        ),
        migrations.AddField(
            model_name='concern',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='concern',
            field=models.ForeignKey(blank=True, db_column='concern', null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Concern'),
        ),
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Company'),
        ),
        migrations.AddField(
            model_name='brand',
            name='concern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goodbuyDatabase.Concern'),
        ),
    ]
