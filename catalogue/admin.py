from django.contrib import admin
from .models import ProjectIdea, Step
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from django import forms


class StepInline(admin.StackedInline):
    model = Step

class ProjectIdeaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        (None, {
            "fields": [
                "name", "slug", "featured", "image",
                ("experience_level", "experience_note"),
                ("effort_level", "effort_note"),
                ("min_required_people", "max_required_people"),
                "description", "example"
                ]
        }),
    ]
    inlines = [StepInline]
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

admin.site.register(ProjectIdea, ProjectIdeaAdmin)
