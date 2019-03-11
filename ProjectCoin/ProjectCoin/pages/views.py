from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .verify import customerForm
from django.http import JsonResponse
from datetime import datetime, timezone
from .graph import get_df

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    if request.method == 'POST':
        verification = customerForm(request.POST)
        if verification.is_valid():
            verification.save()
            return redirect('register')
        else:
            verification =customerForm()
    return render(request,'register.html',{})

def login(request):
    return render(request, "login.html", {})

def about(request):
    return render(request, "about.html",{})

def bitcoin(request):
    return render(request, "bitcoin.html",{})

def litecoin(request):
    return render(request, "litecoin.html",{})

def ethereum(request):
    return render(request, "ethereum.html",{})

def dashboard(request):
    return render(request, "dashboard.html",{})

def get_crypto_data(request, *args):
    coin = request.get_full_path()
    coin = coin[-3:]
    data = get_df(1546290000, 1560000000, coin, "day")
    return JsonResponse(data, safe=False)

def get_year_data(request, *args):
    coin = request.get_full_path()
    # Coin type appended to url
    coin = coin[-3:]
    today = datetime.today()
    # Retrieving Unix Epoch time for get_df function
    timestamp = today.timestamp()
    timestamp = int(timestamp)
    lastyear = timestamp - 86400 * 365
    # "day" passed an argument to get daily data from CryptoCompare
    data = get_df(lastyear, timestamp, coin, "day")
    return JsonResponse(data, safe=False)

def get_month_data(request, *args):
    coin = request.get_full_path()
    # Coin type appended to url
    coin = coin[-3:]
    today = datetime.today()
    # Retrieving Unix Epoch time for get_df function
    timestamp = today.timestamp()
    timestamp = int(timestamp)
    lastmonth = timestamp - 86400 * 30
    # "day" passed an argument to get daily data from CryptoCompare
    data = get_df(lastmonth, timestamp, coin, "day")
    return JsonResponse(data, safe=False)

def get_week_data(request, *args):
    coin = request.get_full_path()
    # Coin type appended to url
    coin = coin[-3:]
    today = datetime.today()
    # Retrieving Unix Epoch time for get_df function
    timestamp = today.timestamp()
    timestamp = int(timestamp)
    lastweek = timestamp - 86400 * 7
    # "day" passed an argument to get daily data from CryptoCompare
    data = get_df(lastweek, timestamp, coin, "day")
    return JsonResponse(data, safe=False)

def get_day_data(request, *args):
    coin = request.get_full_path()
    # Coin type appended to url
    coin = coin[-3:]
    today = datetime.today()
    # Retrieving Unix Epoch time for get_df function
    timestamp = today.timestamp()
    timestamp = int(timestamp)
    yesterday = timestamp - 86400
    # "hour" passed an argument to get hourly data from CryptoCompare
    data = get_df(yesterday, timestamp, coin, "hour")
    return JsonResponse(data, safe=False)

def get_hour_data(request, *args):
    coin = request.get_full_path()
    # Coin type appended to url
    coin = coin[-3:]
    today = datetime.today()
    # Retrieving Unix Epoch time for get_df function
    timestamp = today.timestamp()
    timestamp = int(timestamp)
    lasthour = timestamp - 3600
    # "minute" passed an argument to get minute data from CryptoCompare
    data = get_df(lasthour, timestamp, coin, "minute")
    return JsonResponse(data, safe=False)
