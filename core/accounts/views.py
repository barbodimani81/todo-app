from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views import View

from .forms import ProfileRegistrationForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    fields = "email", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:tasks")


class ProfileRegistrationView(View):
    form_class = ProfileRegistrationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the user and profile
            return redirect('accounts:login')  # Redirect after successful registration
        return render(request, self.template_name, {'form': form})
