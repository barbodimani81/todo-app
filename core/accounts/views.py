# from django.contrib.auth.views import LoginView
# from django.shortcuts import render
#
# from .forms import EmailAuthenticationForm
#
#
# class CustomLoginView(LoginView):
#     form_class = EmailAuthenticationForm
#
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


@login_required
def some_view(request):
    if request.user.is_authenticated:
        return redirect('todo:tasks')  # Redirect to login page if not authenticated
    # Your view logic here


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('login')  # Redirect to the login after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

