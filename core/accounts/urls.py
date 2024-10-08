from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView, ProfileRegistrationView

app_name = 'accounts'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', ProfileRegistrationView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
