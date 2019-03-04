# Generated by Django 2.1.7 on 2019-03-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concern',
            name='rating',
            field=models.CharField(blank=True, choices=[('Neutral', 'Neutral'), ('Ethical', 'Ethical'), ('Unethical', 'Unethical')], help_text='0 = Neutral | 1 = Ethical | 2 = Unethical', max_length=45, null=True),
        ),
    ]