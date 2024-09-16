# from django import forms
# from django.contrib.auth import authenticate
#
#
# class EmailAuthenticationForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         if email and password:
#             user = authenticate(username=email, password=password)
#             if user is None:
#                 raise forms.ValidationError("Invalid login")
#         return self.cleaned_data
