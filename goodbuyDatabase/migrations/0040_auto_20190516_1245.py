# Generated by Django 2.1.7 on 2019-05-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodbuyDatabase', '0039_auto_20190515_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=45, verbose_name='Product Name'),
        ),
    ]