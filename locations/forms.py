from django.forms import ModelForm

from .models import Location


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ("title", "description", "lat", "long")
