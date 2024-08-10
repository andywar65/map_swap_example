from django.db import models
from django.urls import reverse
from djgeojson.fields import PointField


class Location(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    geom = PointField(null=True)
    lat = models.FloatField("Latitude", default=0)
    long = models.FloatField("Longitude", default=0)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

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
