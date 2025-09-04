from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
# Create your views here.
class Task_list(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'