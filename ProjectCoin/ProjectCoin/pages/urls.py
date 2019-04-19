
from django.urls import path
from django.conf.urls import url
from . import views
from .views import get_crypto_data
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.dashboard, name="dashboard"),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="user_logout"),
    path('about/', views.about, name="about"),
    url(r'^register/$', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('bitcoin/', views.bitcoin, name="bitcoin"),
    path('litecoin/', views.litecoin, name="litecoin"),
    path('ethereum/', views.ethereum, name="ethereum"),
    path('dashboard/', views.dashboard, name="dashboard"),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'index.html',}, name='user_logout' ),
    url(r'api/cryptodata/$', get_crypto_data, name='crypto-data')
]
