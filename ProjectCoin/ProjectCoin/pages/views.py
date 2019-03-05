from django.shortcuts import render
from django.http import JsonResponse
from .graph import get_df

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    return render(request, "register.html",{})

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

def get_crypto_data(request, *args):
    coin = request.get_full_path()
    coin = coin[-3:]
    data = get_df(1546290000, 1560000000, coin)
    return JsonResponse(data, safe=False)
