from django.urls import path

from .views import BaseListView, LocationCreateView, LocationDetailView

app_name = "locations"
urlpatterns = [
    path("all/", BaseListView.as_view(), name="base_list"),
    path("add/", LocationCreateView.as_view(), name="location_create"),
    path("<pk>/", LocationDetailView.as_view(), name="location_detail"),
]
