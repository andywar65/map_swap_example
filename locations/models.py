from django.db import models
from djgeojson.fields import PointField


class Location(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    geom = PointField("LatLong")

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
