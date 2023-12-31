from django.db import models

class Task(models.Model):
  description = models.CharField(max_length=200)
  is_completed = models.BooleanField(default=False)
  due_date = models.DateField(null=True, blank=True)

  def __str__(self):
    return self.description
