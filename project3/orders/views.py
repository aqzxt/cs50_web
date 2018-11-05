from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Order, Prices


def index(request):
    return render(request, "orders/index.html")


def register_view(request):
    # Deal with user registration
    reg_username = request.POST.get("reg_username")
    reg_email = request.POST.get("reg_email")
    reg_password = request.POST.get("reg_password")

    if reg_username and reg_email and reg_password:
        user = User.objects.create_user(username=reg_username, email=reg_email, password=reg_password)
        user.save()
        return render(request, "orders/index.html", {"message": "Registration successful"})
    return render(request, "orders/index.html", {"message": "Invalid credentials"})

    

def login_view(request):
    # Deal with user login
    login_username = request.POST.get("login_username")
    login_password = request.POST.get("login_password")
    user = authenticate(request, username=login_username, password=login_password)

    if user is None:
        return render(request, "orders/index.html", {"message": "Invalid credentials"})

    return HttpResponseRedirect(reverse("index"))



def menu(request):
    return render(request, "orders/menu.html")

def myorders(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)

