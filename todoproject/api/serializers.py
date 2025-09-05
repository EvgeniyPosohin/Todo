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