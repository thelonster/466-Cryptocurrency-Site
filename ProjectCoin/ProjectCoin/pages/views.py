from django.shortcuts import render, redirect
from django.http import JsonResponse
from .graph import get_df
from .forms import UserRegister
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
    logged_in = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            logged_in = True
            return render(request, "index.html", {'user_name':username, 'logged_in':logged_in}) 
        else:
            return HttpResponse("Invalid user or password")
    else:
        return render(request, "login.html", {})

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
    data = get_df(1546290000, 1560000000, coin)
    return JsonResponse(data, safe=False)
