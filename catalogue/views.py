import io
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django_weasyprint.views import WeasyTemplateResponseMixin
from django.http import FileResponse
from htmldocx import HtmlToDocx
from .models import ProjectIdea, Attachment

class CatalogueListView(ListView):
    template_name = "catalogue/overview.html"
    model = ProjectIdea
    queryset = ProjectIdea.objects.all().order_by("-featured", "experience_level", "effort_level", "-name")

class CatalogueDetailView(DetailView):
    template_name = "catalogue/detail.html"
    context_object_name = "idea"
    model = ProjectIdea

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