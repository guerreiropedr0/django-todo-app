from django.urls import path

from . import views

app_name="todos"
urlpatterns = [
    path("", views.TaskList.as_view(), name="task-list"),
    path("create/", views.create, name="create"),
]