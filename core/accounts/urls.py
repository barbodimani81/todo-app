from django.urls import path, include

from .views import CustomLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('register/', , name='register'),
]
