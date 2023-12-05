
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.WomenHome.as_view() , name='home'),
    path('about/', views.about, name='about' ),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='show_post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>', views.show_tag, name='tag'),
]