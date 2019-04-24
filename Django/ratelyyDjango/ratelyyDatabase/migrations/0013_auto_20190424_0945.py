# Generated by Django 2.1.7 on 2019-04-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0012_product_stat_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganicCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='gtin',
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Product Name'),
        ),
    ]
