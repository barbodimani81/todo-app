from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView

app_name = 'todo'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('', TaskCreateView.as_view(), name='create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
]
