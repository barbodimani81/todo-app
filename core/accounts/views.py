from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views import View

from .forms import ProfileRegistrationForm, CustomLoginForm


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


class CustomLoginView(View):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Login the user
                login(request, user)
                return redirect('todo:tasks')  # Redirect after successful login
            else:
                form.add_error(None, 'Invalid email or password')

        return render(request, self.template_name, {'form': form})
