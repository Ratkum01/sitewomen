from django import forms
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm
# Create your views here.

# def login_user(request):
#     return HttpResponse('login')
class LoginUser(LoginView):
    form_class= LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}

class RegisterUser(CreateView):
    form_class= RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title':'Registracia'}
    success_url = reverse_lazy('users:login')

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    
    # def get_success_url(self):
    #     return reverse_lazy('home')

# def logout_user(request):
#     return HttpResponse('logout')
