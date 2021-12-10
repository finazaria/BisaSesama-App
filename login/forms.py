from django import forms
from django.db import connection
from passlib.handlers.pbkdf2 import pbkdf2_sha256


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com'}),
        max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=50)
