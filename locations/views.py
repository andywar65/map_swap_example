import json

from django.views.generic import DetailView, ListView

from .models import Location


class HtmxMixin:
    """Switches template depending on request.htmx"""

    def get_template_names(self) -> list[str]:
        if not self.request.htmx:
            return [self.template_name.replace("htmx/", "")]
        return [self.template_name]

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.htmx:
            dict = {"refreshCollections": True}
            response["HX-Trigger-After-Swap"] = json.dumps(dict)
        return response


class BaseListView(HtmxMixin, ListView):
    model = Location
    context_object_name = "markers"
    template_name = "locations/htmx/base_list.html"


class LocationDetailView(HtmxMixin, DetailView):
    model = Location
    template_name = "locations/htmx/location_detail.html"
