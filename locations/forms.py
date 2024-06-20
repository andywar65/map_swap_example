from django.forms import ModelForm

from .models import Location


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ("title", "description", "lat", "long")

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
