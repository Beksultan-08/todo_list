from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("toggle_status/<int:task_id>/", views.toggle_task_status, name="toggle_task_status"),
    path("sorted/", views.sorted_task_list, name="sorted_task_list"),
]
