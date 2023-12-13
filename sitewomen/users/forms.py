from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields= ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username= forms.CharField(label='Login', widget= forms.TextInput(attrs={'class':'form-input'}))
    password1= forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2= forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels= {
            'email':'EMAIL',
            'first_name': "ИМЯ",
            'last_name': 'Фамилия'
        }
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-input'}),
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'})
        }