import io
import json
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django_weasyprint.views import WeasyTemplateResponseMixin
from django.http import FileResponse
from htmldocx import HtmlToDocx
from .models import ProjectIdea, Attachment, OverviewConfiguration, FAQ
from django.urls import reverse
from aktivistisch_web.seo import get_breadcrumb
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

def get_faq_json(faqs):
    if len(faqs) == 0:
        return None

    items = [{"@type": "Question", "name": faq.question, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(faq.answer)}} for faq in faqs]
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": list(items)
    })

class CatalogueListView(ListView):
    template_name = "catalogue/overview.html"
    model = ProjectIdea
    queryset = ProjectIdea.objects.all().filter(draft=False).order_by("-featured", "experience_level", "effort_level", "-name")

    def get_context_data(self, **kwargs):
        context = super(CatalogueListView, self).get_context_data(**kwargs)
        overview = OverviewConfiguration.get_solo()
        context["overview"] = overview
        faqs = FAQ.objects.all().order_by("question")
        context["faq"] = faqs
        context["faq_json"] = get_faq_json(faqs)
        context["meta"] = {
            'title': f"Startseite - {overview.page_title}",
            'url': self.request.build_absolute_uri(),
            'description': overview.page_description
        }
        return context

class CatalogueDetailView(DetailView):
    template_name = "catalogue/detail.html"
    context_object_name = "idea"
    model = ProjectIdea

    queryset = ProjectIdea.objects.all().filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super(CatalogueDetailView, self).get_context_data(**kwargs)
        idea = self.get_object()
        image = None
        if idea.image:
            image = self.request.build_absolute_uri(idea.image.url)
        context["meta"] = {
            'title': f"{idea.name} - Aktiv werden!",
            'url': self.request.build_absolute_uri(),
            'description': mark_safe(strip_tags(idea.description)),
            'breadcrumb': get_breadcrumb([{
                "name": "Projektkatalog",
                "url": self.request.build_absolute_uri(reverse("main"))
            }, {
                "name": idea.name,
                "url": self.request.build_absolute_uri(reverse("idea-detail", kwargs={"slug": idea.slug}))
            }]),
            'image': image
        }
        return context

def old_idea_location_redirect(request, *args, **kwargs):
    return redirect('idea-detail', permanent=True, slug=kwargs['slug'])

class CataloguePDFView(WeasyTemplateResponseMixin, ListView):
    template_name = "catalogue/pdf_catalogue.html"
    model = ProjectIdea
    pdf_filename="Projektkatalog.pdf"
    pdf_attachment=True
    queryset = ProjectIdea.objects.all().order_by("-featured", "experience_level", "effort_level", "-name")

class AttachmentPDFView(WeasyTemplateResponseMixin, DetailView):
    template_name = "catalogue/pdf_attachment.html"
    model = Attachment
    pdf_attachment=True
    queryset = Attachment.objects.all().filter(attachment_type="RESOURCE")

    def get_pdf_filename(self):
        context = self.get_context_data()
        return f"{context['attachment'].name}.pdf"

class AttachmentDOCXView(SingleObjectMixin, View):
    model = Attachment
    queryset = Attachment.objects.all().filter(attachment_type="RESOURCE")

    def get(self, request, *args, **kwargs):
        attachment = self.get_object()
        buffer = io.BytesIO()

        parser = HtmlToDocx()
        docx = parser.parse_html_string(attachment.content)
        docx.save(buffer)

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f"{attachment.name}.docx")