from django.urls import path, include
from .views import HomeView, CreateTaskView, TaskListView


app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateTaskView.as_view(), name='create'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]