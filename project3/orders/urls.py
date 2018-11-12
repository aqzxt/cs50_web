from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("myorders", views.myorders, name="myorders"),
    path("logout", views.logout_view, name="logout")
]
