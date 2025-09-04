from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    task_name = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task_name} {self.id}'