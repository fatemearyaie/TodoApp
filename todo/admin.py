from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date', 'updated_date']
    list_display = ['id', 'task_name', 'created_date', 'updated_date', 'complete']
admin.site.register(Task, TaskAdmin)