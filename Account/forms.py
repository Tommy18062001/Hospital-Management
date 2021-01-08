from django import forms

# we need the user form and model in order to take information about our user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User

        # what are the field that i want to get
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'style': 'width:50%; box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "email": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Email',
                                            'style': 'width:50%; box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),

            "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control'})
        }
