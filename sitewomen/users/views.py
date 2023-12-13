from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import LoginUserForm
# Create your views here.

# def login_user(request):
#     return HttpResponse('login')
class LoginUser(LoginView):
    form_class= LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}
    
    # def get_success_url(self):
    #     return reverse_lazy('home')

# def logout_user(request):
#     return HttpResponse('logout')
