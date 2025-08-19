from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    class Meta:
        unique_together = ('owner', 'name')
        ordering = ['name']

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'todo', 'к выполнению'
        IN_PROGRESS = 'in_progress', 'в процессе'
        DONE = 'done', 'Сделано'

    class Priority(models.IntegerChoices):
        LOW = 1, 'низкий'
        MEDIUM = 2, 'средний'
        HIGH = 3, 'высокий'

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='tasks'
    )
    status = models.CharField(max_length=20, choices=Status.choices,
                              default=Status.TODO
                              )
    priority = models.IntegerField(choices=Priority.choices,
                                   default=Priority.MEDIUM)
    date = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['status', '-priority', 'date', '-create_at']

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        return (
            self.date and self.status != self.Status.DONE
            and self.date < timezone.localdate()
        )