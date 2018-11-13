from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib import messages
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

            # key: tuple (Callable form, non-callable form, callable model)
            "pizza": (forms.PizzaForm(), forms.PizzaForm, models.Pizza()),
            "topping1": (forms.ToppingForm1(), forms.ToppingForm1, models.Topping1()),
            "topping2": (forms.ToppingForm2(), forms.ToppingForm2, models.Topping2()),
            "topping3": (forms.ToppingForm3(), forms.ToppingForm3, models.Topping3()),
            "sub": (forms.SubForm(), forms.SubForm, models.Sub()),
            "pasta": (forms.PastaForm(), forms.PastaForm, models.Pasta()),
            "salad": (forms.SaladForm(), forms.SaladForm, models.Salad()),
            "dinner": (forms.DinnerPlatterForm(), forms.DinnerPlatterForm, models.DinnerPlatter()),

            "order": (forms.OrderForm(), forms.OrderForm),

            # Reference prices table in template
            "regular_p": prices.Prices.regular.values(),
            "sicilian_p": prices.Prices.sicilian.values(),
            "sub_p": prices.Prices.sub.values(),
            "pasta_p": prices.Prices.pasta.values(),
            "salad_p": prices.Prices.salad.values(),
            "dinner_p": prices.Prices.dinner.values(),

            "user": request.user
        }
        if request.method == "POST":

            # Instantiate a new Order(); add username to order
            order = models.Order()
            order.username = request.user.username
            primary_key = ''

            # Loop through additions
            for data in context.items():

                # Context dict never changes, safe to assume when to break the loop
                if data[0] == "regular_p": break

                current_form = data[1][1](request.POST)
                if current_form.is_valid():

                    current_form.save()
                    cleaned = current_form.cleaned_data

                    if cleaned is not None:
                        # Valid "cleaned" output
                        # {'pizzas': 'REG', 'pizza_size': 'S', 'toppings_options': 'SPECIAL'}

                        # Instantiate related model
                        model = data[1][2]

                        is_none = False
                        # Add cleaned data to current model instance and save it to db
                        for item in cleaned.items():
                            # item is a tuple (key, value)
                            
                            if item[1] is None:
                                is_none = True
                                break

                            setattr(model, item[0], item[1])

                        # Make sure there are only valid data
                        if not is_none:
                            model.save()

                            # Store pizza pk: main primary key
                            if data[0] == "pizza": 
                                primary_key = model.pk
                            model.pk = primary_key

                            # Add created model to order
                            setattr(order, data[0], model)

                # else: # In case, there are no valid data submitted
                #     context["message"] = 'Error. You submitted invalid data.'
                #     return render(request, "orders/menu.html", context)

            # Add to cart
            try: my_cart
            except NameError: my_cart = cart.Cart()

            order.pk = primary_key
            my_cart.add_order(primary_key, order)

            print(order)
            cost = prices.Prices()
            cost.get_total(order)

            # Store cart and orders for rendering
            context['get_cart'] = my_cart.get_cart()
            context['get_items_prices'] = cost.cost
            context['get_total'] = cost.total

            return render(request, "orders/myorders.html", context)
            
        # if method == GET
        return render(request, "orders/menu.html", context)
    
    return render(request, "orders/index.html", {"message": 'Your credentials was not valid.'})


def myorders(request):
    if not request.user.is_anonymous:
        # if request.method == "POST":

        context = {
            "orders": models.Order.objects.all(),
            "message": 'Your credentials was not valid.'
        }
        return render(request, "orders/myorders.html", context)

    return render(request, "orders/index.html", {"message": 'Your credentials was not valid.'})