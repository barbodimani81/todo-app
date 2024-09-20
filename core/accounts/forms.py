# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# from .models import User
#
#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ("email",)
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ("email",)
from django import forms
from .models import User, Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']  # Add fields you need


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'description']
