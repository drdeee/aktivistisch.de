from .models import ProjectIdea
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

def last_updated_project_idea():
    return ProjectIdea.objects.order_by("-last_updated").first()

class ProjectIdeaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return ProjectIdea.objects.all().filter(draft=False)

    def lastmod(self, idea):
        return idea.last_updated
    
    def priority(self, idea):
        if(idea.featured):
            return 0.8
        return 0.6
    
    def location(self, idea):
        return reverse("idea-detail", kwargs={"slug": idea.slug})