from django.urls import path

from . import views

app_name="todos"
urlpatterns = [
    path("", views.TaskList.as_view(), name="task-list"),
    path("new/", views.TaskCreate.as_view(), name="task-create"),
    path("<int:pk>/", views.TaskDetail.as_view(), name="task-detail"),
    path("<int:pk>/edit/", views.TaskUpdate.as_view(), name="task-update"),
    path("<int:pk>/delete/", views.TaskDelete.as_view(), name="task-delete"),
]