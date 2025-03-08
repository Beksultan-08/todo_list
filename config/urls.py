from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from task.views import TaskListView




urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('task', include('task.urls', namespace='task')),
]
