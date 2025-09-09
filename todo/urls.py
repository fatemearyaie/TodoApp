from .views import UpdateTask, CreateTask, DeleteTask, TaskComplete, TaskList
from django.urls import path
app_name = 'todo'
urlpatterns = [
    path('tasklist/', TaskList.as_view(), name='tasklist'),
    path('create/', CreateTask.as_view(), name='create'),
    path('update/', UpdateTask.as_view(), name='update'),
    path('delete/', DeleteTask.as_view(), name='delete'),
    path('complete/', TaskComplete.as_view(), name='complete')
]
