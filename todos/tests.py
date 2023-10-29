from django.test import TestCase
from django.urls import reverse

from .models import Task

class TaskIndexViewTests(TestCase):
  def test_no_tasks(self):
    """
    If no tasks exist, an appropriate message is displayed.
    """
    response = self.client.get(reverse("todos:index"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No todos are available.")
    self.assertQuerySetEqual(response.context["task_list"], [])

  def test_with_task(self):
    """
    The todos index page may display one task.
    """
    task = Task.objects.create(description="Task.")
    response = self.client.get(reverse("todos:index"))
    self.assertQuerySetEqual(
        response.context["task_list"],
        [task],
    )

  def test_multiple_tasks(self):
    """
    The todos index page may display multiple tasks.
    """
    task1 = Task.objects.create(description="Task 1.")    
    task2 = Task.objects.create(description="Task 2.")    
    response = self.client.get(reverse("todos:index"))
    self.assertQuerySetEqual(
        response.context["task_list"],
        [task1, task2],
    )
