from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ["description"]

    widgets = {
      "description": forms.TextInput(attrs={ "class": "form-control" })
    }

    labels = {
      "description": "Task Description"
    }