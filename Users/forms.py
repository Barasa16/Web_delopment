from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    Firstname = forms.CharField(max_length=100)
    Lastname = forms.CharField(max_length=100)
    Company = forms.CharField(max_length=100)
    Position = forms.CharField(max_length=100)
    Email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "Firstname",
            "Lastname",
            "username",
            "Email",
            "Company",
            "Position",
            "password1",
            "password2",
        ]

