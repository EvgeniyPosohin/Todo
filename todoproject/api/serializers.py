from django.contrib.auth import get_user_model
from rest_framework import serializers
from task.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "owner", "description", "status",
                  "priority", "date", "create_at", "update_at",)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("owner", "name")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)