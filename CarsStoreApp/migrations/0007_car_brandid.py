# Generated by Django 4.0.5 on 2022-06-02 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarsStoreApp', '0006_carmodel_brandid'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='BrandID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsStoreApp.brand'),
        ),
    ]