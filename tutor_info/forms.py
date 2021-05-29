from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms):
    username = forms.CharField(label="Юзернейм", help_text="Юзернейм може мати букви, цифри та знаки @/./+/-/_ ")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Підтвердіть пароль", help_text='Введіть пароль ще раз',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
