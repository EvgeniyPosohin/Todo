from django.contrib.gis.geos.prototypes import geos_equals
from rest_framework import generics
from task.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetalTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

