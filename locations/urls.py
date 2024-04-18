from django.urls import path

from .views import BaseListView, LocationDetailView

app_name = "locations"
urlpatterns = [
    path("all/", BaseListView.as_view(), name="base_list"),
    path("<pk>/", LocationDetailView.as_view(), name="location_detail"),
]
