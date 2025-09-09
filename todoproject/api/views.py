from django.contrib.auth import get_user_model
from django.contrib.gis.geos.prototypes import geos_equals
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from task.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer, UserSerializer
from rest_framework import viewsets


# class TaskApiCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class CategoryApiCreate(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# # UPDATE/Desrtoy
# class DetalTaskApiUpdate(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class CategoryApiUpdate(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # lookup_field = 'owner'
#
# class UserApiList(generics.ListAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset =  get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetalApiUpdate(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset =  get_user_model().objects.all()
#     serializer_class = UserSerializer

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



