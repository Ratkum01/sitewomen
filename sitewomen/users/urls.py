from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView , PasswordChangeDoneView

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login' ),
    path('register/', views.RegisterUser.as_view(), name= 'register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change' ),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done')
]