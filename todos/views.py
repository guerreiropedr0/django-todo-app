from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

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
  
class TaskUpdate(generic.UpdateView):
  model = Task
  fields = '__all__'  
  template_name_suffix = "_update_form"

  def form_valid(self, form):
    self.object = form.save()

    return render(self.request, "snippets/task.html", { "task": self.object })

class TaskDelete(generic.DeleteView):
    model = Task

    def delete(self, request, *args, **kwargs):
      self.object = self.get_object()


      self.object.delete()

      # Tells the client to render nothing (delete row)
      return HttpResponse(status=200)