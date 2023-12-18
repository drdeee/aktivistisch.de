from django.views.generic import ListView, DetailView
from .models import ProjectIdea


class CatalogueListView(ListView):
    template_name = "catalogue/overview.html"
    model = ProjectIdea
    queryset = ProjectIdea.objects.all().order_by("-featured", "experience_level", "effort_level", "-name")

class CatalogueDetailView(DetailView):
    template_name = "catalogue/detail.html"
    context_object_name = "idea"
    model = ProjectIdea