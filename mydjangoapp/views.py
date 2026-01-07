from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User


# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def product_details(request):
    products = DressDetails.objects.all()
    return render(request, 'products.html', {"productDetails":products})

def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def signup_handler(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                return redirect("signup")
            else:
                userinfo = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                userinfo.save()
                return redirect("login")
        else:
            return redirect("signup")
            
        