from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from colorfield.fields import ColorField

class ProjectIdea(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    draft = models.BooleanField(default=True)

    experience_level = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ], help_text="0... none, 5... a lot")

    effort_level = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], help_text="1... minimal, 5... noch")

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
        try:
            if self.image != None:
                return f"background-image: linear-gradient(0deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 66%),url({self.image.url});"
            return ""
        except:
            return ""
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

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

class OverviewConfiguration(SingletonModel):
    title = models.CharField(max_length=100)
    overview_text = RichTextField()
    impressum_text = RichTextField()

    page_title = models.CharField(max_length=100)
    page_description = models.TextField(max_length=500)

    def __str__(self):
        return "Overview Configuration"
    
    class Meta:
        verbose_name = "Overview Configuration"

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = RichTextField()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Party(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(format="hex")
    border = models.BooleanField(default=False)
    order_by = models.IntegerField(default=0)

    @property
    def contrast_color(self):
        color = self.color[1:]

        hex_red = int(color[0:2], base=16)
        hex_green = int(color[2:4], base=16)
        hex_blue = int(color[4:6], base=16)

        if (hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722) > 140:
            return "#000000"
        else:
            return "#ffffff"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Parties"
        ordering = ["order_by"]


class Prediction(models.Model):
    name = models.CharField(max_length=100)
    visible = models.BooleanField(default=False)
    order_by = models.IntegerField(default=0)

    parties = models.ManyToManyField(Party, through='PredictionPercentage')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order_by"]

    

class PredictionPercentage(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ["party__order_by"]