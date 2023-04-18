from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework import generics
from .models import Todo 
from .serializers import TodoSerializer 
from rest_framework.exceptions import NotFound



# Create your views here.

class TodoList(generics.ListCreateAPIView):
    serializer_class= TodoSerializer
    queryset = Todo.objects.all()

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_object(self):
        try:
            obj = super().get_object()
        except Http404:
            raise NotFound("Object not found / detail is deleted. ")
        return obj






