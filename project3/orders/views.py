from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Order, Prices


def index(request):

    if request.method == "POST":
        # Get user data from the register form and save it
        reg_username = request.POST.get("reg_username")
        reg_email = request.POST.get("reg_email")
        reg_password = request.POST.get("reg_password")

        if reg_username and reg_email and reg_password:
            # If actual user data then save it to db
            reg_user = User.objects.create_user(username=reg_username, email=reg_email, password=reg_password)
            reg_user.save()
            return render(request, "orders/index.html", {"message": "You have successfully registered."})
            

        # Get user data from the login form and save it
        login_username = request.POST.get("login_username")
        login_password = request.POST.get("login_password")

        login_user = authenticate(request, username=login_username, password=login_password)

        # Make sure user is registered then proceed to log him/her in
        if login_user is not None:
            login(request, login_user)
            return HttpResponseRedirect(reverse("menu"))

        # Otherwise, display message
        return messages.error(request, 'Your credentials was not valid.')

    # If method == GET
    return render(request, "orders/index.html")


def menu(request):
    return render(request, "orders/menu.html")

def myorders(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)

def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "You have logged out successfully."})