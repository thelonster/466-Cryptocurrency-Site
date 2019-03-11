from django.shortcuts import render, redirect
from django.http import JsonResponse
from .graph import get_df
from .forms import UserRegister
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    registered=False
    if request.method == 'POST':
        user_form = UserRegister(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegister()
    return render(request, "register.html", {'user_form':user_form, 'registered':registered})

#def login(request):
    #return render(request, "login.html", {})

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
    data = get_df(1546290000, 1560000000, coin)
    return JsonResponse(data, safe=False)
