
from django.urls import path
from django.conf.urls import url
from . import views
from .views import get_crypto_data, get_year_data, get_month_data, get_week_data, get_day_data, get_hour_data

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="user_logout"),
    url(r'^register/$', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('coins/', views.coins, name="coins"),
    path('bitcoin/', views.bitcoin, name="bitcoin"),
    path('litecoin/', views.litecoin, name="litecoin"),
    path('ethereum/', views.ethereum, name="ethereum"),
    path('dashboard/', views.dashboard, name="dashboard"),
    url(r'api/cryptodata/$', get_crypto_data, name='crypto-data'),
    url(r'api/yeardata/$', get_year_data, name='year-data'),
    url(r'api/monthdata/$', get_month_data, name='month-data'),
    url(r'api/weekdata/$', get_week_data, name='week-data'),
    url(r'api/daydata/$', get_day_data, name='day-data'),
    url(r'api/hourdata/$', get_hour_data, name='hour-data')
]
