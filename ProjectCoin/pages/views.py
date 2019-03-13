from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email = email, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login.html')
    return render(request, "login.html", {})

def about(request):
    return render(request, "about.html",{})

def bitcoin(request):
    return render(request, "bitcoin.html",{})

def litecoin(request):
    return render(request, "litecoin.html",{})

def dashboard(request):
    if not request.user.is_authenicated():
        return redirect('login.html')
    return render(request, "dashboard.html", {})