from django.http import HttpResponse
from django.shortcuts import render

from .models import Order

# Create your views here.
def index(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)
