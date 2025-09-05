from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Task, Category
from .forms import TaskForm, CategoryForm


def logout_view(request):
    logout(request)
    return redirect()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт создан. Войдите, пожалуйста.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        qs = Task.objects.filter(owner=self.request.user).select_related('category')
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')
        category = self.request.GET.get('category')
        priority = self.request.GET.get('priority')

        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if status:
            qs = qs.filter(status=status)
        if category:
            qs = qs.filter(category_id=category)
        if priority:
            qs = qs.filter(priority=priority)
        return qs


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task_list')
    template_name = 'task/task_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Задача создана.')
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task_list')
    template_name = 'task/task_form.html'

    def get_queryset(self):
        # ограничиваем доступ только задачами владельца
        return Task.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Задача обновлена.')
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task:task_list')
    template_name = 'task/task_confirm_delete.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('task:task_list')
    template_name = 'task/category_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Категория создана.')
        return super().form_valid(form)