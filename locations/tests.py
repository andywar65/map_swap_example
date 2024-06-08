from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

pword = settings.DJANGO_SUPERUSER_PASSWORD


class LocationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\nTest Location views")
        User.objects.create_user("user", "user@example.com", pword)
