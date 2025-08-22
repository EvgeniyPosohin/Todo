from django.utils import timezone
from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'category', 'priority', 'status', 'date']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.localdate():
            raise forms.ValidationError('Дедлайн не может быть в прошлом.')
        return date

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']