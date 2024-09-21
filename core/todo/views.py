from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from .forms import TaskForm
from .models import Task


# class HomeView(TemplateView):
#     template_name = 'todo/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Welcome to todo app!"
#         return context


class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    success_url = '/todo/tasks'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'
    ordering = '-id'
    paginate_by = 3


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.all()


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/todo/tasks/'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

