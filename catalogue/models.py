from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField


class ProjectIdea(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
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

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_as_background(self):
        if self.image != None:
            return f"background-image: linear-gradient(0deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 30%, rgba(0,0,0,0) 56%),url({self.image.url});"
        return ""

class Step(models.Model):
    project_idea = models.ForeignKey(ProjectIdea, related_name='steps', on_delete=models.CASCADE)

    name = models.CharField(max_length=300)
    content = RichTextField()