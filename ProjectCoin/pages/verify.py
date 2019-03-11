from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class customerForm(forms.Form):
    email = forms.CharField(label='Enter email', min_length=7, max_length=200)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confPass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def check_email(self):
        email = self.cleaned_data['email'].lower()
        duplicate_email = User.objects.filter(email=email)
        if duplicate_email.count():
            raise ValidationError("Email already exist")
        return email

    def check_password(self):
        password = self.cleaned_data.get('password')
        confPass = self.cleaned_data.get('confPass')

        if password and confPass and password != confPass:
            raise ValidationError("Password do not match")
        return confPass

    def save_user(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user