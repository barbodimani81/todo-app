from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .forms import TaskForm
from .models import Task


class HomeView(TemplateView):
    template_name = 'todo/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Welcome to todo app!"
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/todo/tasks/'

    def form_valid(self, form):
        form.instance.author = self.request.user


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.all()



