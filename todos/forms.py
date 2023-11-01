from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
      model = Task
      fields = "__all__"
      widgets = {
        "due_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        "description": forms.TextInput(attrs={"class": "form-control"}),
        "is_completed": forms.Select(choices=[
          (False, 'Pending'),
          (True, 'Completed'),
        ], attrs={'class': 'form-select'})
      }
