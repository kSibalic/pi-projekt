from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Unesite ime',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Unesite lozinku',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Unesite ime',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Unesite email',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Unesite lozinku',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ponovite unos lozinke',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))