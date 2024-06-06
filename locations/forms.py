from django.forms import ModelForm, NumberInput

from .models import Location


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ("title", "description", "lat", "long")
        widgets = {
            "lat": NumberInput(
                attrs={
                    "max": 90.0,
                    "min": -90.0,
                }
            ),
            "long": NumberInput(
                attrs={
                    "max": 180.0,
                    "min": -180.0,
                }
            ),
        }
