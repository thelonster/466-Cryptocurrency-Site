from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .verify import customerForm

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

