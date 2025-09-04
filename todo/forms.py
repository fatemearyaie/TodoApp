from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control rounded-4',
            'name': 'task_name',
            'placeholder' : 'enter the task name'
        }
    ),
    label='',)
    class meta:
        model = Task
        fields = ('task_name',)