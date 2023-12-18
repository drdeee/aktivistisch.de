from django.contrib import admin
from .models import ProjectIdea, Step
from django import forms


class StepInline(admin.StackedInline):
    model = Step

class ProjectIdeaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        (None, {
            "fields": [
                "name", "slug", "featured", 
                ("experience_level", "experience_note"),
                ("effort_level", "effort_note"),
                ("min_required_people", "max_required_people"),
                ("description", "example")
                ]
        }),
    ]
    inlines = [StepInline]

admin.site.register(ProjectIdea, ProjectIdeaAdmin)
admin.site.register(Step)
