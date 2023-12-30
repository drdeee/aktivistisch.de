from django.contrib import sitemaps
from django.urls import reverse
from catalogue.sitemap import last_updated_project_idea, ProjectIdeaSitemap

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "monthly"

    itemsDict = {
        "main": 1
    }

    def items(self):
        # return keys of items dict
        return list(self.itemsDict.keys())

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.itemsDict[item]

    def lastmod(self, item):
        if(item == "main"):
            return last_updated_project_idea().last_updated
            

site_infos = {
    "static": StaticViewSitemap,
    "project_ideas": ProjectIdeaSitemap
}