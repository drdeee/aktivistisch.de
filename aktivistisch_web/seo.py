from django.contrib import sitemaps
from django.urls import reverse
from catalogue.sitemap import last_updated_project_idea, ProjectIdeaSitemap
import json

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "monthly"

    itemsDict = {
        "main": 1,
        "impressum": 0.1
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

def get_breadcrumb(items):
    breadcrumb_items = []

    index = 0
    for item in items:
        index += 1
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": index,
            "name": item["name"],
            "item": item["url"]
    })

    return json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_items
    })