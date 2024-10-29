from rest_framework.routers import DefaultRouter

from .views import TodoModelViewSet

app_name = 'api-v1'


router = DefaultRouter()
router.register('tasks', TodoModelViewSet, basename='tasks')
urlpatterns = router.urls
