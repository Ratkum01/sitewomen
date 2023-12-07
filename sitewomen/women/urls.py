
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.WomenHome.as_view() , name='home'),
    path('about/', views.about, name='about' ),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='show_post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>', views.WomenTag.as_view(), name='tag'),
]