# Generated by Django 2.1.7 on 2019-04-29 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0025_auto_20190429_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'managed': True, 'ordering': ('name', 'id')},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'managed': True, 'ordering': ('name', 'id'), 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='concern',
            options={'managed': True, 'ordering': ('name', 'id')},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True, 'ordering': ('name', 'id'), 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'ordering': ('name', 'id')},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'managed': True, 'ordering': ('name', 'id')},
        ),
    ]
