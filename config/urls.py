from django.contrib import admin
from django.urls import path, include
from task.views import task_list

urlpatterns = [
    path('', task_list, name='home'),
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('account/', include('account.urls')),
]