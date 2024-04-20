from django.db import models
from django.urls import reverse
from djgeojson.fields import PointField


class Location(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    geom = PointField("LatLong")

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.title

    @property
    def popupContent(self):
        url = reverse(
            "locations:location_detail",
            kwargs={"pk": self.id},
        )
        title_str = '<a class="link link-primary" href="#" '
        title_str += (
            "onclick=\"openLocation('%(url)s')\"><strong>%(title)s</strong></a>"
            % {
                "title": self.title,
                "url": url,
            }
        )
        return {"content": title_str}
