from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CategoryCreateView)


app_name = 'task'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'), #TaskListView.as_view()
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
]