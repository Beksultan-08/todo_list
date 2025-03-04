from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        # Фильтрация по статусу
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        # Фильтрация по приоритету
        priority_filter = self.request.GET.get('priority')
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)
        # Сортировка (по дедлайну, приоритету или статусу)
        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['deadline', 'priority', 'status']:
            queryset = queryset.order_by(sort_by)
        return queryset

@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@login_required
def change_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    statuses = [choice[0] for choice in Task.STATUS_CHOICES]
    try:
        current_index = statuses.index(task.status)
        new_index = (current_index + 1) % len(statuses)
        task.status = statuses[new_index]
        task.save()
    except ValueError:
        pass
    return redirect('task_list')
