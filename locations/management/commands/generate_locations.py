from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from faker import Faker
from faker.providers import geo

from locations.models import Location


class Command(BaseCommand):
    help = "Seed database with location sample data."

    @transaction.atomic
    def handle(self, *args, **options):
        if settings.DEBUG is False:
            raise CommandError("This command cannot be run when DEBUG is False.")
        self.stdout.write("Seeding database with Locations...")
        create_items()

        self.stdout.write("Done.")


def create_items():
    fake = Faker()
    fake.add_provider(geo)
    for i in range(10):
        loc = fake.location_on_land()
        Location.objects.create(
            title=loc[2],
            description=fake.sentence(),
            geom={"type": "Point", "coordinates": [float(loc[0]), float(loc[1])]},
        )
