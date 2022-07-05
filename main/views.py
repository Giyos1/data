from django.shortcuts import render
from django.views.generic import ListView

from main.models import DataArchitect


class HomepageView(ListView):
    model = DataArchitect
    context_object_name = "data"
    template_name = "list.html"
