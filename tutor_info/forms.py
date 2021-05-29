from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Юзернейм", help_text="Юзернейм може мати букви, цифри та знаки @/./+/-/_ ")
    email = forms.EmailField(label="E-mail")


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
