from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .serializers import TaskSerializer
from ...models import Task
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination


class TodoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'author': ["in", "exact"], 'title': ["exact"], 'done': ["exact"]}
    search_fields = ['title', 'description']
    ordering_fields = ['title']
    pagination_class = DefaultPagination

