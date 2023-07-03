from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePagueView(TemplateView):
    template_name = "core/home.html"

class ContactPagueView(TemplateView):
    template_name = "core/contact.html"

