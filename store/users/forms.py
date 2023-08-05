from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """Фщрма регистрации нового пользователя"""
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'from-input'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Meta:
        models = User
        fields = ('username', 'email', 'password1', 'password2')
