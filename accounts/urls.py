from .views import RegisterView, LoginView, task_list
from django.urls import path
 
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('task_list', task_list, name='task_list')
]
