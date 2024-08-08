from django.urls import path
from . import views

urlpatterns = [
    path('photo/', views.Photo, name='photo'),
    path('shop/', views.Shop, name='shop'),
    path('link/', views.Link, name='link'),
    path('avatar/', views.Avatar, name='avatar'),
    path('', views.homework_login, name='home_login'),
    path('register/', views.homework_register, name='register'),
    path('welcome/', views.homework_home_page, name='home_page'),

]
