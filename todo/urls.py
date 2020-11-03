from django.urls import path
from . import views

urlpatterns = [
    path("", views.taskList, name="task-list"),
    path("create-task", views.createTask, name="create-task"),
    path("edit-task/<int:pk>", views.editTask, name="edit-task"),
    path("delete-task/<int:pk>", views.deleteTask, name="delete-task")
]