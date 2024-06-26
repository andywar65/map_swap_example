# Generated by Django 5.0.6 on 2024-06-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0002_location_lat_location_long"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.DecimalField(
                decimal_places=6, max_digits=9, null=True, verbose_name="Latitude"
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="long",
            field=models.DecimalField(
                decimal_places=6, max_digits=9, null=True, verbose_name="Longitude"
            ),
        ),
    ]
