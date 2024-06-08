from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from faker.providers import geo

from .models import Location

pword = settings.DJANGO_SUPERUSER_PASSWORD


class LocationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\nTest Location views")
        User.objects.create_user("user", "user@example.com", pword)
        fake = Faker()
        fake.add_provider(geo)
        for i in range(2):
            loc = fake.location_on_land()
            Location.objects.create(
                title=loc[2],
                description=fake.sentence(),
                lat=float(loc[0]),
                long=float(loc[1]),
                geom={"type": "Point", "coordinates": [float(loc[1]), float(loc[0])]},
            )

    def test_view_status_no_login(self):
        print("\n-Test status without logging")
        response = self.client.get(reverse("locations:base_list"))
        self.assertEqual(response.status_code, 200)
        print("\n--Test base list status 200")
        response = self.client.get(
            reverse("locations:location_detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test location detail status 200")
        response = self.client.get(reverse("locations:location_create"))
        self.assertEqual(response.status_code, 302)
        print("\n--Test location create status 302")
        response = self.client.get(
            reverse("locations:location_update", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        print("\n--Test location update status 302")
        response = self.client.get(
            reverse("locations:location_delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        print("\n--Test location delete status 302")

    def test_view_status_login(self):
        print("\n-Test status logged")
        self.client.login(username="user", password=pword)
        response = self.client.get(reverse("locations:location_create"))
        self.assertEqual(response.status_code, 200)
        print("\n--Test location create status 200")
        response = self.client.get(
            reverse("locations:location_update", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test location update status 200")
        response = self.client.get(
            reverse("locations:location_delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 404)
        print("\n--Test location delete status 404")

    def test_view_status_htmx(self):
        print("\n-Test status with HTMX header")
        response = self.client.get(
            reverse("locations:base_list"), headers={"HX-Request": "true"}
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test with htmx base list status 200")
        response = self.client.get(
            reverse("locations:location_detail", kwargs={"pk": 1}),
            headers={"HX-Request": "true"},
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test with htmx location detail status 200")
        self.client.login(username="user", password=pword)
        response = self.client.get(
            reverse("locations:location_create"), headers={"HX-Request": "true"}
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test with htmx location create status 200")
        response = self.client.get(
            reverse("locations:location_update", kwargs={"pk": 1}),
            headers={"HX-Request": "true"},
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test with htmx location update status 200")
        response = self.client.get(
            reverse("locations:location_delete", kwargs={"pk": 1}),
            headers={"HX-Request": "true"},
        )
        self.assertEqual(response.status_code, 200)
        print("\n--Test with htmx location delete status 200")

    def test_CRUD_cycle(self):
        print("\n-Test CRUD cycle")
        self.client.login(username="user", password=pword)
        response = self.client.post(
            reverse("locations:location_create"),
            {
                "title": "Here",
                "description": "This is where we are",
                "lat": 42.0,
                "long": 12.0,
            },
            follow=True,
        )
        last = Location.objects.last()
        self.assertRedirects(
            response,
            reverse("locations:location_detail", kwargs={"pk": last.id}),
            status_code=302,
            target_status_code=200,
        )
        print("\n--Test create location redirect")
        self.assertEqual(last.title, "Here")
        print("\n--Test correct location creation")
        response = self.client.post(
            reverse("locations:location_update", kwargs={"pk": last.id}),
            {
                "title": "Here",
                "description": "This is where where",
                "lat": 42.1,
                "long": 12.0,
            },
            follow=True,
        )
        self.assertRedirects(
            response,
            reverse("locations:location_detail", kwargs={"pk": last.id}),
            status_code=302,
            target_status_code=200,
        )
        print("\n--Test update location redirect")
        response = self.client.get(
            reverse("locations:location_delete", kwargs={"pk": last.id}),
            headers={"HX-Request": "true"},
        )
        last = Location.objects.last()
        self.assertNotEqual(last.title, "Here")
        print("\n--Test correct location deletion")

    def test_model_str_method(self):
        first = Location.objects.first()
        self.assertEqual(first.__str__(), first.title)
