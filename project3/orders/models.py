from django.db import models

# Every item
class Order(models.Model):
    type = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    toppings = models.CharField(max_length=60, default="")
    additions = models.CharField(max_length=60, default="")

    def __str__(self):
        if self.toppings and self.additions:
            return f"{self.size} {self.type} pizza with {self.toppings} and {self.additions}"
        if self.toppings:
            return f"{self.size} {self.type} pizza with {self.toppings}"
        else:
            return f"{self.size} {self.type} pizza and {self.additions}"