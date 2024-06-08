from django.db import models
from django.urls import reverse
from djgeojson.fields import PointField


class Location(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    geom = PointField(null=True)
    lat = models.FloatField("Latitude")
    long = models.FloatField("Longitude")

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    __o_lat = None
    __o_long = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__o_lat = self.lat
        self.__o_long = self.long

    def save(self, *args, **kwargs):
        if self.lat != self.__o_lat or self.long != self.__o_long:
            self.geom = {
                "type": "Point",
                "coordinates": [
                    self.long,
                    self.lat,
                ],
            }
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("locations:location_detail", kwargs={"pk": self.id})

    @property
    def popupContent(self):
        url = self.get_absolute_url()
        title_str = '<a class="link link-primary" href="#" '
        title_str += (
            "onclick=\"openLocation('%(url)s')\"><strong>%(title)s</strong></a>"
            % {
                "title": self.title,
                "url": url,
            }
        )
        return {"content": title_str}
