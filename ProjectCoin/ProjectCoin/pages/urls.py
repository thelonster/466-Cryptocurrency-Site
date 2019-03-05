
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('bitcion/', views.bitcoin, name="bitcoin"),
    path('litecoin/', views.litecoin, name="litecoin"),
    path('dashboard/', views.dashboard, name="dashboard"),
]

