"""
URL configuration for aktivistisch_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalogue.views import CatalogueListView, CatalogueDetailView, CataloguePDFView, AttachmentPDFView, AttachmentDOCXView

urlpatterns = [
    path('', CatalogueListView.as_view(), name="main"),
    path('idea/<slug:slug>/', CatalogueDetailView.as_view(), name="idea-detail"),
    path('download/catalogue', CataloguePDFView.as_view()),
    path('download/attachment/<int:pk>.pdf', AttachmentPDFView.as_view(), name="attachment-pdf"),
    path('download/attachment/<int:pk>.docx', AttachmentDOCXView.as_view(), name="attachment-docx"),
]
