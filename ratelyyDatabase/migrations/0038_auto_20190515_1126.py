# Generated by Django 2.1.7 on 2019-05-15 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0037_auto_20190514_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Corporation Name')),
                ('logo', models.URLField(blank=True, null=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Country')),
            ],
            options={
                'db_table': 'corporations',
                'ordering': ('name', 'id'),
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='concern',
            name='origin',
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'managed': True, 'ordering': ('corporation', 'id')},
        ),
        migrations.RemoveField(
            model_name='brand',
            name='concern',
        ),
        migrations.RemoveField(
            model_name='company',
            name='concern',
        ),
        migrations.RemoveField(
            model_name='product',
            name='concern',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='concern',
        ),
        migrations.DeleteModel(
            name='Concern',
        ),
        migrations.AddField(
            model_name='brand',
            name='corporation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Corporation'),
        ),
        migrations.AddField(
            model_name='company',
            name='corporation',
            field=models.ForeignKey(blank=True, db_column='corporation', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Corporation'),
        ),
        migrations.AddField(
            model_name='product',
            name='corporation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Corporation'),
        ),
        migrations.AddField(
            model_name='rating',
            name='corporation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Corporation'),
        ),
    ]
