from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Location


@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    list_display = ("title",)
