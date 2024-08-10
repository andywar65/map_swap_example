from django.forms import FloatField, ModelForm, NumberInput

from .models import Location


class LocationCreateForm(ModelForm):
    lat = FloatField(
        label="Latitude", widget=NumberInput(attrs={"max": 90, "min": -90})
    )
    long = FloatField(
        label="Longitude", widget=NumberInput(attrs={"max": 180, "min": -180})
    )

    class Meta:
        model = Location
        fields = ("title", "description")

    def clean(self):
        cleaned_data = super().clean()
        if "lat" not in cleaned_data:
            cleaned_data["lat"] = 0
        if "long" not in cleaned_data:
            cleaned_data["long"] = 0
        lat = cleaned_data["lat"]
        long = cleaned_data["long"]
        if lat > 90 or lat < -90:
            self.add_error("lat", "Invalid value")
        if long > 180 or long < -180:
            self.add_error("long", "Invalid value")
        return cleaned_data
