from django.urls import path

from .views import (
    LocationCreateView,
    LocationDetailView,
    LocationListView,
    LocationUpdateView,
    location_delete_view,
)

app_name = "locations"
urlpatterns = [
    path("all/", LocationListView.as_view(), name="base_list"),
    path("add/", LocationCreateView.as_view(), name="location_create"),
    path("<pk>/", LocationDetailView.as_view(), name="location_detail"),
    path("<pk>/update/", LocationUpdateView.as_view(), name="location_update"),
    path("<pk>/delete/", location_delete_view, name="location_delete"),
]
