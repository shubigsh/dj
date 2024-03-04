from django.shortcuts import render
from django.http import HttpResponse
from .models import kylie
from .models import Lakme
from .models import MAC
from .models import Nykaa
#assingment
def index(request):
    return render(request,'index.html')
def diff_exa(request):
    return render(request,'diff_exa.html')
def www(request):
    return render(request,'www.html')
def pakages(request):
    return render(request,'pakages.html')
def dij(request):
    return render(request,'dij.html')
def boot(request):
    return render(request,'boot.html')
#project 1
def home(request):
    return render(request,'home.html')

def lakme(request):
    products=Lakme.objects.all()
    return render(request,'Lakme.html',{'Lakme':products})

def mac(request):
    products=MAC.objects.all()
    return render(request,'MAC.html',{'MAC':products})

def nykaa(request):
    products=Nykaa.objects.all()
    return render(request,'Nykaa.html',{'Nykaa':products})
def Kylie(request):
    products = kylie.objects.all()
   
    return render(request, 'kylie.html', {'kylie':products})

def beauty_tips(request):
    return render(request,'beauty_tips.html')

def cart(request):
    cart_data = request.session.get('cart', [])
    return render(request, 'cart.html', {'cart_data': cart_data})

#project 2 views








