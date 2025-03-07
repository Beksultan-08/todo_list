from django.urls import path
from task.views import task_list, add_task, edit_task, delete_task, toggle_task_status, sorted_task_list

app_name = "task"

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/add/', add_task, name='add_task'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('task/toggle_status/<int:task_id>/', toggle_task_status, name='toggle_task_status'),
    path('tasks/sorted/', sorted_task_list, name='sorted_task_list'),
]
