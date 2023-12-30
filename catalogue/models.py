from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class ProjectIdea(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)

    experience_level = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    experience_note = models.TextField(max_length=100, null=True, blank=True)

    effort_level = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    effort_note = models.TextField(max_length=100, null=True, blank=True)

    min_required_people = models.IntegerField(validators=[
            MinValueValidator(1)
        ])
    max_required_people = models.IntegerField(null=True, blank=True, )
    max_required_people = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ]
    )

    description = RichTextField()
    example = RichTextField(null=True, blank=True)

    image = models.ImageField(upload_to="images", null=True, blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def image_as_background(self):
        if self.image != None:
            return f"background-image: linear-gradient(0deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 66%),url({self.image.url});"
        return ""

    @property
    def downloads(self):
        return Attachment.objects.filter(project_idea=self, attachment_type="DOWNLOAD")

    def resources(self):
        return Attachment.objects.filter(project_idea=self, attachment_type="RESOURCE")

class Step(models.Model):
    project_idea = models.ForeignKey(ProjectIdea, related_name='steps', on_delete=models.CASCADE)

    name = models.CharField(max_length=300)
    content = RichTextField()

class Attachment(models.Model):
    project_idea = models.ForeignKey(ProjectIdea, related_name='attachments', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=30)


    class AttachmentType(models.TextChoices):
        RESSOURCE = "RESOURCE", _("Resource")
        DOWNLOAD  = "DOWNLOAD", _("Download")
    attachment_type = models.CharField(max_length=9, choices=AttachmentType.choices, default=AttachmentType.RESSOURCE)

    content = RichTextField(null=True, blank=True)
    file = models.FileField(upload_to='attachments', null=True, blank=True)

    @property
    def file_type(self):
        if self.file:
            return self.file.name.lower().split(".")[-1]
        return ""