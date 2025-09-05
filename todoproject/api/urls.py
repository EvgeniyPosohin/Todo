from django.urls import path
from .views import TaskApiView, CategoryApiView, DetalTask

app_name = 'api'

urlpatterns = [
    path('task/', TaskApiView.as_view()),
    path('task/<int:pk>/', DetalTask.as_view()),
    path('category/', CategoryApiView.as_view()),
    ]