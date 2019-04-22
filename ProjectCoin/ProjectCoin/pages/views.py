from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .verify import customerForm
from django.http import JsonResponse
from datetime import datetime, timezone
from .graph import get_df
from .forms import UserRegister

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    registered=False
    if request.method == 'POST':
        user_form = UserRegister(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegister()
    return render(request, "register.html", {'user_form':user_form, 'registered':registered})

def user_login(request):
    #logged_in = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            #logged_in = True
            return render(request, "index.html") 
            #return HttpResponse(user.username);
        else:
            return HttpResponse("Invalid user or password")
    else:
        return render(request, "login.html", {})

def coins(request):
    return render(request, "coins.html",{})

def about(request):
    return render(request, "about.html",{})

def bitcoin(request):
    return render(request, "bitcoin.html",{})

def litecoin(request):
    return render(request, "litecoin.html",{})

def ethereum(request):
    return render(request, "ethereum.html",{})
@login_required
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
