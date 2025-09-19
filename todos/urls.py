from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>', DetailTodo.as_view()),
    path('<int:pk>/delete', DeleteTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('<int:pk>/update', UpdateTodo.as_view()),
]
