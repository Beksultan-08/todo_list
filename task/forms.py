from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'status']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}) }