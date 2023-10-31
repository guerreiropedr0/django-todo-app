from django.views import generic
from django.shortcuts import render

from .models import Task

class TaskList(generic.ListView):
  template_name = "todos/task_list.html"
  model = Task

class TaskCreate(generic.CreateView):
  model = Task
  fields = "__all__"

  def form_valid(self, form):
    self.object = form.save()

    return render(self.request, "snippets/task.html", { "task": self.object })