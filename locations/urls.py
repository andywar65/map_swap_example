from django.urls import path

from .views import BaseListView

app_name = "locations"
urlpatterns = [
    path("all/", BaseListView.as_view(), name="base_list"),
]
