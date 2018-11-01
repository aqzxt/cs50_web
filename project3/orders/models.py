from django.db import models

# Create your models here.
class Order(models.Model):
    type = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    toppings = models.CharField(max_length=60)
    additions = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.size} {self.type} pizza with {self.toppings} and {self.additions}"