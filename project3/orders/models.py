from django.db import models

# Individual items
class Pizza(models.Model):
    '''Represents the main order: pizza.'''
    PIZZA = (
        ('REG', 'Regular'),
        ('SIC', 'Sicilian')
    )
    SIZE = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    TOPPING_OPTIONS = (
        ('CHEESE', 'Cheese'),
        ('SPECIAL', 'Special (Surprise! ;)'),
        ('1', '1 Topping (Pick)'),
        ('2', '2 Toppings (Pick)'),
        ('3', '3 Toppings (Pick)')
    )
    pizzas = models.CharField(max_length=10, choices=PIZZA)
    pizza_size = models.CharField(max_length=5, choices=SIZE)
    toppings_options = models.CharField(max_length=10, choices=TOPPING_OPTIONS)

    def __str__(self):
        return f"[{self.id}] {self.pizza_size} {self.pizzas} Pizza"

class Topping1(models.Model):
    '''Represents a topping addition. Default value is NULL'''

    # Keep track of how many toppings was added
    # instances = []

    # def __init__(self, f=0):
    #     self.f = f
    #     Topping.instances.append(self)

    TOPPINGS = (
        ('ANCHOVIES', 'Anchovies'), ('ARTICHOKE', 'Artichoke'), 
        ('BARBECUE CHICKEN', 'Barbecue Chicken'),
        ('BLACK OLIVES', 'Black Olives'),
        ('BUFFALO CHICKEN', 'Buffalo Chicken'),
        ('CANADIAN BACON', 'Canadian Bacon'), 
        ('EGGPLANT', 'Eggplant'), ('FRESH GARLIC', 'Fresh Garlic'), 
        ('GREEN PEPPERS', 'Green Peppers'), ('HAM', 'Ham'), 
        ('HAMBURGER', 'Hamburger'), ('MUSHROOMS', 'Mushrooms'), 
        ('ONIONS', 'Onions'), ('PEPPERONI', 'Pepperoni'), 
        ('PINEAPPLE', 'Pineapple'), ('SAUSAGE', 'Sausage'), 
        ('SPINACH', 'Spinach'), ('TOMATO_BASIL', 'Tomato & Basil'), 
        ('ZUCCHINI', 'Zucchini')
    )
    # Maximum of 3 toppings are allowed
    # if len(instances) < 3:
    toppings = models.CharField(max_length=60, null=True, blank=True, choices=TOPPINGS)

    # if topping == 'CHEESE' or topping == 'SPECIAL':
    #     c = 3

    def __str__(self):
        return f"[{self.id}] {self.toppings} Topping1"

class Topping2(Topping1):
    def __str__(self):
        return f"[{self.id}] {self.toppings} Topping2"

class Topping3(Topping1):
    def __str__(self):
        return f"[{self.id}] {self.toppings} Topping3"
    

class Sub(models.Model):
    '''Represents a submarine sandwich addition. Default value is NULL'''
    # su_prices = {
    #     'CHEESE':(6.50, 7.95), 'CHEESEBURGER':(5.10, 7.45), 
    #     'CHICKEN PARM':(7.50, 8.50), 'EGGPLANT PARM':(6.50, 7.95), 
    #     'FRIED CHICKEN':(6.95, 8.50), 'HAM_CHEESE':(6.50, 7.95), 
    #     'HAMBURGER':(4.60, 6.95), 'ITALIAN':(6.50, 7.95),
    #     'MEATBALL':(6.50, 7.95), 'STEAK':(6.50, 7.95),
    #     'STEAK_CHEESE':(6.95, 8.50), 'STEAK_GREEN PEPPERS':(7.45, 9.00), 
    #     'STEAK_MUSHROOMS':(7.45, 9.00), 'STEAK_ONIONS':(7.45, 9.00), 
    #     'TUNA':(6.50, 7.95), 'TURKEY':(7.50, 8.50),
    #     'VEGGIE':(6.95, 8.50), 'SAPEON':(0, 8.50),
    #     'XCHEESE':(0.50, 0.50)
    # }
    
    SUBS = (
        ('CHEESE', 'Cheese'), ('CHEESEBURGER', 'Cheeseburger'), 
        ('CHICKEN PARM', 'Chicken Parmigiana'),
        ('EGGPLANT PARM', 'Eggplant Parmigiana'), 
        ('XCHEESE', 'Extra Cheese on any subs'),
        ('FRIED CHICKEN', 'Fried Chicken'), ('HAM_CHEESE', 'Ham + Cheese'),
        ('HAMBURGER', 'Hamburger'), ('ITALIAN', 'Italian'),
        ('MEATBALL', 'Meatball'), ('SAPEON', 'Sausage, Peppers & Onions'),
        ('STEAK', 'Steak'), ('STEAK_CHEESE', 'Steak + Cheese'),
        ('STEAK_GPEPPERS', 'Steak + Green Peppers'), 
        ('STEAK_MUSHROOMS', 'Steak + Mushrooms'),
        ('STEAK_ONIONS', 'Steak + Onions'), 
        ('TUNA', 'Tuna'), ('TURKEY', 'Turkey'), ('VEGGIE', 'Veggie')
    )
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    subs = models.CharField(max_length=60, null=True, blank=True, choices=SUBS)
    sub_size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)

    def __str__(self):
        return f"[{self.id}] {self.sub_size} {self.subs} Subs"

class Pasta(models.Model):
    '''Represents a pasta addition. Default value is NULL'''
    # p_prices = {
    #     'BZ MOZZARELA': 6.50,
    #     'BZ MEATBALLS': 8.75,
    #     'BZ CHICKEN': 9.75
    # }
    PASTAS = (
        ('BZ MOZZARELLA', 'Baked Ziti w/ Mozzarella'),
        ('BZ MEATBALLS', 'Baked Ziti w/ Meatballs'),
        ('BZ CHICKEN', 'Baked Ziti w/ Chicken')
    )
    pastas = models.CharField(max_length=60, null=True, blank=True, choices=PASTAS)

    def __str__(self):
        return f"[{self.id}] {self.pastas} Pasta"

class Salad(models.Model):
    '''Represents a salad addition. Default value is NULL'''
    # sa_prices = {
    #     'GARDEN': 6.25,
    #     'GREEK': 8.25,
    #     'ANTIPASTO': 8.25,
    #     'TUNA': 8.25
    # }
    SALADS = (
        ('GARDEN','Garden Salad'),
        ('GREEK', 'Greek Salad'),
        ('ANTIPASTO', 'Antipasto'),
        ('TUNA', 'Salad w/ Tuna')
    )
    salads = models.CharField(max_length=60, null=True, blank=True, choices=SALADS)

    def __str__(self):
        return f"[{self.id}] {self.salads} Salad"

class DinnerPlatter(models.Model):
    '''Represents a dinner platter addition. Default value is NULL'''
    # d_prices = {
    #     # type: (price small, price large)
    #     'GARDEN SALAD': (35.00, 60.00),
    #     'GREEK SALAD': (45.00, 70.00),
    #     'ANTIPASTO': (45.00, 70.00),
    #     'BAKED ZITI': (35.00, 60.00),
    #     'MEAT PARM': (45.00, 70.00),
    #     'CHICKEN PARM': (45.00, 80.00)
    # }

    DINNERS = (
        ('GARDEN SALAD','Garden Salad'),
        ('GREEK SALAD', 'Greek Salad'),
        ('ANTIPASTO', 'Antipasto'),
        ('BAKED ZITI', 'Baked Ziti'),
        ('MEAT PARM', 'Meatball Parm'),
        ('CHICKEN PARM', 'Chicken Parm')
    )
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    dinners = models.CharField(max_length=60, null=True, blank=True, choices=DINNERS)
    dinner_size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)

    def __str__(self):
        return f"[{self.id}] {self.dinner_size} {self.dinners} Dinner Platter"

# All items
class Order(models.Model):
    '''Represents a single order'''
    pizza = models.ForeignKey(Pizza, on_delete="models.CASCADE", related_name="pizzas_list")
    topping1 = models.ForeignKey(Topping1, on_delete="models.SET_NULL", related_name="toppings_list1", null=True, blank=True)
    topping2 = models.ForeignKey(Topping2, on_delete="models.SET_NULL", related_name="toppings_list2", null=True, blank=True)
    topping3 = models.ForeignKey(Topping3, on_delete="models.SET_NULL", related_name="toppings_list3", null=True, blank=True)
    sub = models.ForeignKey(Sub, on_delete="models.SET_NULL", related_name="subs_list", null=True, blank=True)
    pasta = models.ForeignKey(Pasta, on_delete="models.SET_NULL", related_name="pastas_list", null=True, blank=True)
    salad = models.ForeignKey(Salad, on_delete="models.SET_NULL", related_name="salads_list", null=True, blank=True)
    dinner = models.ForeignKey(DinnerPlatter, on_delete="models.SET_NULL", related_name="dinners_list", null=True, blank=True)
    username = models.CharField(max_length=60)

    def __str__(self):
        '''Format string if the optional addition is available. Default value: empty string'''

        # Check for instance class presence
        t1 = t2 = t3 = su = p = sa = d = ""
        if self.topping1: t1 = f" + {self.topping1}"
        if self.topping2: t2 = f" + {self.topping2}"
        if self.topping3: t3 = f" + {self.topping3}"
        if self.sub: su = f" + {self.sub}"
        if self.pasta: p = f" + {self.pasta}"
        if self.salad: sa = f" + {self.salad}"
        if self.dinner: d = f" + {self.dinner}"
        
        return f"Order from {self.username}: [{self.id}] {self.pizza}{t1}{t2}{t3}{su}{p}{sa}{d}"
