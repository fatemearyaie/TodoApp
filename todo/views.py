from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_form.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
class CreateTask(CreateView):
    model = Task
    fields = ['task_name']
    success_url = reverse_lazy('tasklist')
    template_name = 'task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdateTask(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('tasklist')
    template_name = 'todo/update_task.html'

class DeleteTask(DeleteView):
    model = Task
    success_url = 'todo/delete_task.html'
    context_object_name = 'tasks'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy('tasklist')

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)