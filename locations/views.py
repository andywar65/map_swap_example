import json
from typing import Any

from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Location


class HxTemplateMixin:
    """Switches template depending on request.htmx"""

    def get_template_names(self) -> list[str]:
        if not self.request.htmx:
            return [self.template_name.replace("htmx/", "")]
        return [self.template_name]


class HxSetupMixin:
    """Restricts to HTMX requests"""

    def setup(self, request, *args, **kwargs):
        if not request.htmx:
            raise Http404("Request without HTMX headers")
        super().setup(request, *args, **kwargs)


class BaseListView(HxTemplateMixin, ListView):
    model = Location
    context_object_name = "markers"
    template_name = "locations/htmx/base_list.html"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.htmx:
            dict = {"refreshCollections": True}
            response["HX-Trigger-After-Swap"] = json.dumps(dict)
        return response


class LocationDetailView(HxTemplateMixin, DetailView):
    model = Location
    template_name = "locations/htmx/location_detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["markers"] = self.object
        return context

    def dispatch(self, request, *args, **kwargs):
        response = super(LocationDetailView, self).dispatch(request, *args, **kwargs)
        if request.htmx:
            dict = {"refreshCollections": True}
            response["HX-Trigger-After-Swap"] = json.dumps(dict)
        return response
