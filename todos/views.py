from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo


# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodo(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer