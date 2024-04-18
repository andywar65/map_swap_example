from factory import Faker
from factory.django import DjangoModelFactory

from .models import Location


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Location

    description = Faker("lorem")
