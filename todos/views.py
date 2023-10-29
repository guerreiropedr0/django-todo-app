from django.http import HttpResponse
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
  template_name = "todos/index.html"
  model = Task