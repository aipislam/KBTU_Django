from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Product, Category, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer
from .models import Product, Category
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms

def get_index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product_list(request):
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    products = Product.objects.all()
    
    if category:
        products = products.filter(category__name=category)
    
    if min_price:
        products = products.filter(price__gte=min_price)
    
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'product_list.html', {'products': products})


# Create your views here.

def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


def logout_view(request):
    logout(request)
    return redirect("main-home")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect("main-home")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})