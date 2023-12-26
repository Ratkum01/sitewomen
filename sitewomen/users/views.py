from django import forms
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView , PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import LoginUserForm, ProfileUserForm, RegisterUserForm, UserPasswordChangeForm
from django.views.generic.edit import UpdateView
from sitewomen import settings
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

class ProfileUser(LoginRequiredMixin, UpdateView):
    model= get_user_model()
    form_class =ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title':'Profile users',
                     'default_image': settings.DEFAULT_USER_IMAGE,
                     }
    
    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    title = ("Password change")
    