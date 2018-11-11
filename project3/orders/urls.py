from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("orders_cart", views.orders_cart, name="orders_cart"),
    path("logout", views.logout_view, name="logout")
]
