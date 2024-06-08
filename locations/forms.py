from django.core.exceptions import ValidationError
from django.forms import ModelForm, NumberInput

from .models import Location


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ("title", "description", "lat", "long")
        widgets = {
            "lat": NumberInput(
                attrs={
                    "max": 90,
                    "min": -90,
                }
            ),
            "long": NumberInput(
                attrs={
                    "max": 180,
                    "min": -180,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        lat = cleaned_data["lat"]
        long = cleaned_data["long"]
        if lat > 90 or lat < -90 or long > 180 or long < -180:
            raise ValidationError("Invalid latlong entry", code="invalid_latlong")
        return cleaned_data
