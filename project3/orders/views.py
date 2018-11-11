from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import models, cart, prices, forms


def index(request):
    if not request.user.is_anonymous:
        return render(request, "orders/menu.html", {"message": "Welcome back"})

    # if not request.user.is_anonymous and request.method == "POST":
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
        return render(request, "orders/index.html", {"message": 'Your credentials was not valid.'})

    # If method == GET
    return render(request, "orders/index.html")


def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "You have logged out successfully."})


def menu(request):

    if not request.user.is_anonymous:

        context = {
            # Rerefence both callable (for template use) and non-callable (for use just below)
            "pizza": (forms.PizzaForm(), None),
            "topping1": (forms.ToppingForm1(), forms.ToppingForm1),
            "topping2": (forms.ToppingForm2(), forms.ToppingForm2),
            "topping3": (forms.ToppingForm3(), forms.ToppingForm3),
            "sub": (forms.SubForm(), forms.SubForm),
            "pasta": (forms.PastaForm(), forms.PastaForm),
            "salad": (forms.SaladForm(), forms.SaladForm),
            "dinner": (forms.DinnerPlatterForm(), forms.DinnerPlatterForm),
            "order": (forms.OrderForm(), forms.OrderForm),

            # Reference prices table in template
            "Regular_p": prices.Prices.regular.items(),
            "Sicilian_p": prices.Prices.sicilian.items(),
            "Sub_p": prices.Prices.sub.items(),
            "Pasta_p": prices.Prices.pasta.items(),
            "Salad_p": prices.Prices.salad.items(),
            "Dinner_p": prices.Prices.dinner.items(),

            "user": request.user
        }
        if request.method == "POST":
            pizza_form = forms.PizzaForm(request.POST)

            # If form data is valid redirect user to shopping cart page
            if pizza_form.is_valid():
                new_pizza = pizza_form.save()
                
                # Instantiate a new Order() and store primary key
                order = models.Order()
                order.pk = new_pizza.pk

                # Convert form data to readable, instantiate Pizza() and add it to order
                pizza_clean = pizza_form.cleaned_data.get('pizza')
                pizza = models.Pizza(pizza_clean)
                order.pizza = pizza

                # Add username to order
                order.username = get_user_model

                # Loop through additions
                for data in context.items():

                    # Skip first
                    if data[0] == "pizza": continue
                    # Break loop when necessary
                    if data[0] == "Regular_p": break

                    current = data[1](request.POST)
                    if current.is_valid():

                        # Add Pizza pk to order instance and save
                        current.pk = new_pizza.pk
                        current.save()

                        cleaned = current.cleaned_data.get(data[0])
                        if cleaned is not None:

                            # If valid data, then add to order
                            setattr(order, data[0], cleaned)

                # Add to cart
                try:
                    my_cart
                except NameError:
                    my_cart = cart.Cart()

                my_cart.add_order(new_pizza.pk, order)
                context["cart"] = my_cart
                    
                return render(request, "orders/cart.html", context)

        # if method == GET
        return render(request, "orders/menu.html", context)
    
    return render(request, "orders/index.html", {"message": 'Your credentials was not valid.'})


def orders_cart(request):
    context = {
        "orders": models.Order.objects.all(),
        "message": 'Your credentials was not valid.'
    }
    if not request.user.is_anonymous:
        # if request.method == "POST":
        return render(request, "orders/myorders.html", context)

    return render(request, "orders/index.html", context)