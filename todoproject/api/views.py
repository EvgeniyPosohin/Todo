from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly
from task.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer, UserSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
