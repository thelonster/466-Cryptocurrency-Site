
from django.urls import path
from django.conf.urls import url
from . import views
from .views import get_crypto_data, get_year_data, get_month_data, get_week_data, get_day_data, get_hour_data, get_multiple_data
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="user_logout"),
    url(r'^register/$', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('coins/', views.coins, name="coins"),
      
    # 10 coin pages
    #changed the path on the website from /coin-name to /coins/coin-name
    path('coins/bitcoin/', views.bitcoin, name="bitcoin"),
    path('coins/litecoin/', views.litecoin, name="litecoin"),
    path('coins/bitcoincash/', views.bitcoincash, name="bitcoincash"),
    path('coins/0x/', views.Ox, name="0x"),
    path('coins/basic-attention-token/', views.attn, name="attn"),
    path('coins/xrp/', views.xrp, name="xrp"),
    path('coins/zcash/', views.zcash, name="zcash"),
    path('coins/stellar/', views.stellar, name="stellar"),
    path('coins/ethereum/', views.ethereum, name="ethereum"),
    path('coins/ethereum-classic/', views.eclassic, name="eclassic"),

    path('dashboard/', views.dashboard, name="dashboard"),
    url(r'api/cryptodata/$', get_crypto_data, name='crypto-data'),
    url(r'api/yeardata/$', get_year_data, name='year-data'),
    url(r'api/monthdata/$', get_month_data, name='month-data'),
    url(r'api/weekdata/$', get_week_data, name='week-data'),
    url(r'api/daydata/$', get_day_data, name='day-data'),
    url(r'api/hourdata/$', get_hour_data, name='hour-data'),
    url(r'api/multipledata/$', get_multiple_data, name='multi-data')
]
