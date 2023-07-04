from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project

# Create your views here.
class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project


