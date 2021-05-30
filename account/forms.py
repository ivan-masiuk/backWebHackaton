from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Ім'я")
    last_name = forms.CharField(label="Фамілія")
    username = forms.CharField(label="Юзернейм")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Підтвердіть пароль",
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Паролі не збігаються!')
        return cd['password2']


class ProfileRegisterForm(forms.ModelForm):
    third_name = forms.CharField(label="По-батькові")
    phone_number = PhoneNumberField(label="Номер телефону")
    photo = forms.ImageField(label='Аватар')

    class Meta:
        model = Profile
        fields = ('third_name', 'phone_number', 'photo')
