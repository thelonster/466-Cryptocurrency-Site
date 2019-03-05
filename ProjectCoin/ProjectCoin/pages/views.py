from django.shortcuts import render

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

def dashboard(request):
    return render(request, "dashboard.html",{})
