from django.db import models

# Individual items
class Pizza(models.Model):
    TYPES = (
        ('R', 'Regular'),
        ('S', 'Sicilian')
    )
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    type = models.CharField(max_length=3, choices=TYPES)
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return f"({self.id}) {self.size} {self.type}"

class Toppings(models.Model):
    TOPPINGS = (
        ('A1', 'Anchovies'), ('A2', 'Artichoke'), 
        ('B1', 'Barbecue Chicken'), ('B2', 'Black Olives'), 
        ('B3', 'Buffalo Chicken'), ('C1', 'Canadian Bacon'), 
        ('E1', 'Eggplant'), ('F1', 'Fresh Garlic'), 
        ('G1', 'Green Peppers'), ('H1', 'Ham'), 
        ('H2', 'Hamburger'), ('M1', 'Mushrooms'), 
        ('O1', 'Onions'), ('P1', 'Pepperoni'), 
        ('P2', 'Pineapple'), ('S1', 'Sausage'), 
        ('S2', 'Spinach'), ('T1', 'Tomato & Basil'), 
        ('Z1', 'Zucchini')
    )
    topping = models.CharField(max_length=2, null=True, blank=True, choices=TOPPINGS)

    def __str__(self):
        return f"({self.id}) {self.topping}"
    

class Subs(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    SUBS = (
        ('C1', 'Cheese'), ('C2', 'Cheeseburger'), 
        ('C3', 'Chicken Parmigiana'), ('E1', 'Eggplant Parmigiana'), 
        ('E2', 'Extra Cheese on any subs'), ('F1', 'Fried Chicken'), 
        ('H1', 'Ham + Cheese'), ('H2', 'Hamburger'), 
        ('I1', 'Italian'), ('M1', 'Meatball'), 
        ('S1', 'Sausage, Peppers & Onions'), ('S2', 'Steak'), 
        ('S3', 'Steak + Cheese'), ('S4', 'Steak + Green Peppers'), 
        ('S5', 'Steak + Mushrooms'), ('S6', 'Steak + Onions'), 
        ('T1', 'Tuna'), ('T2', 'Turkey'), ('V1', 'Veggie')
    )
    subs = models.CharField(max_length=3, null=True, blank=True, choices=SUBS)
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)

    def __str__(self):
        return f"({self.id}) {self.subs}"

class Pasta(models.Model):
    PASTA = (
        ('M2', 'Baked Ziti w/ Mozzarella'),
        ('M1', 'Baked Ziti w/ Meatballs'),
        ('C1', 'Baked Ziti w/ Chicken')
    )
    pasta = models.CharField(max_length=2, null=True, blank=True, choices=PASTA)

    def __str__(self):
        return f"({self.id}) {self.pasta}"

class Salad(models.Model):
    SALADS = (
        ('G1','Garden Salad'),
        ('G2', 'Greek Salad'),
        ('AP', 'Antipasto'),
        ('ST', 'Salad w/ Tuna')
    )
    salad = models.CharField(max_length=2, null=True, blank=True, choices=SALADS)

    def __str__(self):
        return f"({self.id}) {self.salad}"

class DinnerPlatters(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    DINNER = (
        ('G1','Garden Salad'),
        ('G2', 'Greek Salad'),
        ('AP', 'Antipasto'),
        ('BZ', 'Baked Ziti'),
        ('MP', 'Meatball Parm'),
        ('CP', 'Chicken Parm')
    )
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)
    dinner = models.CharField(max_length=2, null=True, blank=True, choices=DINNER)

    def __str__(self):
        return f"({self.id}) {self.size} {self.dinner}"

# All items
class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete="models.CASCADE", related_name="p")
    pizza_size = models.ForeignKey(Pizza, on_delete="models.CASCADE", related_name="p_size")
    topping = models.ForeignKey(Toppings, on_delete="models.SET_NULL", related_name="topping_add", null=True, blank=True)
    sub = models.ForeignKey(Subs, on_delete="models.SET_NULL", related_name="subs_add", null=True, blank=True)
    pasta = models.ForeignKey(Pasta, on_delete="models.SET_NULL", related_name="pasta_add", null=True, blank=True)
    salad = models.ForeignKey(Salad, on_delete="models.SET_NULL", related_name="salad_add", null=True, blank=True)
    dinner = models.ForeignKey(DinnerPlatters, on_delete="models.SET_NULL", related_name="dinner_add", null=True, blank=True)
    dinner_size = models.ForeignKey(DinnerPlatters, on_delete="models.SET_NULL", related_name="dinner_size_add", null=True, blank=True)

    def __str__(self):
        return f"{self.pizza_size} {self.pizza} Pizza - {self.topping} - {self.sub} - {self.pasta} - {self.salad} - {self.dinner}"