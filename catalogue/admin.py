from django.contrib import admin
from .models import ProjectIdea, Step, Attachment, OverviewConfiguration, FAQ, Party, Prediction, PredictionPercentage, ContactFormEntry
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from django import forms
from solo.admin import SingletonModelAdmin


class StepInline(admin.StackedInline):
    model = Step
    classes = ['collapse']

class AttachmentInline(admin.StackedInline):
    model = Attachment
    classes = ['collapse']

class ProjectIdeaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        (None, {
            "fields": [
                "name", "slug", "featured", "draft", "image", "experience_level", "effort_level",
                ("min_required_people", "max_required_people"),
                "description", "example"
                ]
        }),
    ]
    inlines = [StepInline, AttachmentInline]
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

admin.site.register(ProjectIdea, ProjectIdeaAdmin)
admin.site.register(OverviewConfiguration, SingletonModelAdmin)
admin.site.register(FAQ)

class PredictionPercentageInline(admin.StackedInline):
    model = PredictionPercentage

class PredictionAdmin(admin.ModelAdmin):
    inlines = [PredictionPercentageInline]

admin.site.register(Party)
admin.site.register(Prediction, PredictionAdmin)

admin.site.register(ContactFormEntry)