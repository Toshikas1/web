from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
User = get_user_model() 
class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter username"
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter your email"
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter password"
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Confirm Password"
    }))
    class Meta():
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter username"
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter password"
    }))
class EditForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter username"
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter your email"
    }))
    class Meta():
        model = User
        fields = [
            "username",
            "email"
        ]
class PasswordForm(forms.Form):
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter old password"
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Enter password"
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "Confirm Password"
    }))
    class Meta():
        model = User
        fields = [
            "password",
            "password1",
            "password2"
        ]