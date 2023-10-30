from django.views import generic
from django.shortcuts import render

from .models import Task
from .forms import TaskForm

class IndexView(generic.ListView):
  template_name = "todos/index.html"
  model = Task

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in extra context
    context["form"] = TaskForm()
    return context

def create(request):
  task = Task(description=request.POST['description'])
  task.save()
  return render(request, 'snippets/task.html', { "task": task })

  