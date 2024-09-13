from django.urls import path
from .views import HomeView, TaskCreateView, TaskListView, TaskDetailView

app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
