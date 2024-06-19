from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Location


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ("title", "description", "lat", "long")

    def clean(self):
        cleaned_data = super().clean()
        if "lat" not in cleaned_data:
            raise ValidationError("Invalid Latitude entry", code="invalid_lat")
        if "long" not in cleaned_data:
            raise ValidationError("Invalid Longitude entry", code="invalid_long")
        lat = cleaned_data["lat"]
        long = cleaned_data["long"]
        if lat > 90 or lat < -90:
            self.add_error("lat", "Invalid value")
        if long > 180 or long < -180:
            self.add_error("long", "Invalid value")
        return cleaned_data
