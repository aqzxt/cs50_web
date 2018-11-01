from django.db import models

# Create your models here.
class Order(models.Model):
    type = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    toppings = models.CharField(max_length=60)
    additions = models.CharField(max_length=60)




