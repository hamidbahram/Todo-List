from rest_framework import generics 
from todoapp.models import Task
from todoapp.api.serializers import (
    TaskListSerializer, 
    TaskDetailSerializer, 
    TaskCreateSerializer, 
    TaskDeleteSerializer,
    TaskDeleteUpdateSerializer,
)


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    lookup_field = 'id'

class TaskDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteSerializer
    lookup_field = 'id'

class TaskDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteUpdateSerializer
    lookup_field = 'id'