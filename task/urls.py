from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, change_status

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/change_status/', change_status, name='change_status'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns += [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('account/', include('account.urls')),
]