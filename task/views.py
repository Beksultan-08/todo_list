from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from task.models import Task
from task.forms import TaskForm
from django.views.generic import ListView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'task': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})



def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task/task_list')
    else:
        form = TaskForm(instance=task)
        return redirect('task/task_list', {'form':form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task/task_list')


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task/task_list')


def sorted_task_list(request):
    sort_by = request.GET.get('sort_by', 'created_at')  # Параметр сортировки
    tasks = Task.objects.all().order_by(sort_by)
    return render(request, 'task/task_list.html', {'task': tasks})

