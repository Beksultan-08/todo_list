from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task
from account.models import User

# 📝 Форма для добавления и редактирования задачи
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'status']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# 👤 Форма для регистрации
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'age', 'password1', 'password2']

# 🔑 Форма для авторизации
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput())

# ⚙️ Форма для редактирования профиля
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'age']
