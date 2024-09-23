from django import forms
from .models import User, Profile


class ProfileRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'description', 'image']

    def save(self, commit=True):
        # Create User
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        # Create Profile
        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data.get('image')
        )

        if commit:
            user.save()
            profile.save()
        return user, profile


class CustomLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

