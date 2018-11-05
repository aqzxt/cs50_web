from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_view", views.login_view, name="login_view"),
    path("register_view", views.register_view, name="register_view"),
    path("menu", views.menu, name="menu"),
    path("myorders", views.myorders, name="myorders")
]
