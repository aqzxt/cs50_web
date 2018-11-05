from django.db import models
from itertools import count

# Individual items
class Pizza(models.Model):
    '''Represents the main order: pizza.'''
    TYPES = (
        ('REG', 'Regular'),
        ('SIC', 'Sicilian')
    )
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    type = models.CharField(max_length=10, choices=TYPES)
    size = models.CharField(max_length=5, choices=SIZES)

    def __str__(self):
        return f"[{self.id}] {self.size} {self.type} Pizza"

class Topping(models.Model):
    '''Represents a topping addition. Default value is NULL'''

    # Keep track of how many toppings was added
    instances = []

    def __init__(self, f):
        self.f = f
        Topping.instances.append(self)

    TOPPINGS = (
        ('ANCHOVIES', 'Anchovies'), ('ARTICHOKE', 'Artichoke'), 
        ('BARBECUE CHICKEN', 'Barbecue Chicken'),
        ('BLACK OLIVES', 'Black Olives'), ('CHEESE', 'Cheese'),
        ('BUFFALO CHICKEN', 'Buffalo Chicken'),
        ('CANADIAN BACON', 'Canadian Bacon'), 
        ('EGGPLANT', 'Eggplant'), ('FRESH GARLIC', 'Fresh Garlic'), 
        ('GREEN PEPPERS', 'Green Peppers'), ('HAM', 'Ham'), 
        ('HAMBURGER', 'Hamburger'), ('MUSHROOMS', 'Mushrooms'), 
        ('ONIONS', 'Onions'), ('PEPPERONI', 'Pepperoni'), 
        ('PINEAPPLE', 'Pineapple'), ('SAUSAGE', 'Sausage'), 
        ('SPINACH', 'Spinach'), ('TOMATO_BASIL', 'Tomato & Basil'), 
        ('ZUCCHINI', 'Zucchini'), ('SPECIAL', 'Special')
    )
    # Maximum of 3 toppings are allowed
    if len(instances) < 3:
        topping = models.CharField(max_length=60, null=True, blank=True, choices=TOPPINGS)

    # if topping == 'CHEESE' or topping == 'SPECIAL':
    #     c = 3

    def __str__(self):
        return f"[{self.id}] {self.topping} Topping"
    

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
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
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
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)
    type = models.CharField(max_length=60, null=True, blank=True, choices=SUBS)

    def __str__(self):
        return f"[{self.id}] {self.size} {self.type} Subs"

class Pasta(models.Model):
    '''Represents a pasta addition. Default value is NULL'''
    # p_prices = {
    #     'BZ MOZZARELA': 6.50,
    #     'BZ MEATBALLS': 8.75,
    #     'BZ CHICKEN': 9.75
    # }
    PASTA = (
        ('BZ MOZZARELLA', 'Baked Ziti w/ Mozzarella'),
        ('BZ MEATBALLS', 'Baked Ziti w/ Meatballs'),
        ('BZ CHICKEN', 'Baked Ziti w/ Chicken')
    )
    pasta = models.CharField(max_length=60, null=True, blank=True, choices=PASTA)

    def __str__(self):
        return f"[{self.id}] {self.pasta} Pasta"

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
    salad = models.CharField(max_length=60, null=True, blank=True, choices=SALADS)

    def __str__(self):
        return f"[{self.id}] {self.salad} Salad"

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

    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    DINNER = (
        ('GARDEN SALAD','Garden Salad'),
        ('GREEK SALAD', 'Greek Salad'),
        ('ANTIPASTO', 'Antipasto'),
        ('BAKED ZITI', 'Baked Ziti'),
        ('MEAT PARM', 'Meatball Parm'),
        ('CHICKEN PARM', 'Chicken Parm')
    )
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)
    type = models.CharField(max_length=60, null=True, blank=True, choices=DINNER)

    def __str__(self):
        return f"[{self.id}] {self.size} {self.type} Dinner Platter"

# All items
class Order(models.Model):
    '''Represents a single order'''
    pizza = models.ForeignKey(Pizza, on_delete="models.CASCADE", related_name="pizzas")
    topping = models.ForeignKey(Topping, on_delete="models.SET_NULL", related_name="toppings", null=True, blank=True)
    sub = models.ForeignKey(Sub, on_delete="models.SET_NULL", related_name="subs", null=True, blank=True)
    pasta = models.ForeignKey(Pasta, on_delete="models.SET_NULL", related_name="pastas", null=True, blank=True)
    salad = models.ForeignKey(Salad, on_delete="models.SET_NULL", related_name="salads", null=True, blank=True)
    dinner = models.ForeignKey(DinnerPlatter, on_delete="models.SET_NULL", related_name="dinners", null=True, blank=True)

    def __str__(self):
        '''Format string if the optional addition is available. Default value: empty string'''

        # Check for instance class presence
        t = su = p = sa = d = ""
        if self.topping: t = f" + {self.topping}"
        if self.sub: su = f" + {self.sub}"
        if self.pasta: p = f" + {self.pasta}"
        if self.salad: sa = f" + {self.salad}"
        if self.dinner: d = f" + {self.dinner}"
        
        return f"[{self.id}] {self.pizza}{t}{su}{p}{sa}{d}"


class Prices:
    '''Prices for pizzas and its additions'''
    def __init__(self):
        # dict = {type: (price for small, price for large)}
        self.regular = {
            'CHEESE':(12.20, 17.45),
            '1 TOPPINGS':(13.20, 19.45),
            '2 TOPPINGS':(14.70, 21.45),
            '3 TOPPINGS':(15.70, 23.45),
            'SPECIAL':(17.25, 25.45)
        }
        self.sicilian = {
            'CHEESE':(23.45, 37.70),
            '1 TOPPINGS':(25.45, 39.70),
            '2 TOPPINGS':(27.45, 41.70),
            '3 TOPPINGS':(28.45, 43.70),
            'SPECIAL':(29.45, 44.70)
        }
        self.sub = {
            'CHEESE':(6.50, 7.95), 'CHEESEBURGER':(5.10, 7.45), 
            'CHICKEN PARM':(7.50, 8.50), 'EGGPLANT PARM':(6.50, 7.95), 
            'FRIED CHICKEN':(6.95, 8.50), 'HAM_CHEESE':(6.50, 7.95), 
            'HAMBURGER':(4.60, 6.95), 'ITALIAN':(6.50, 7.95),
            'MEATBALL':(6.50, 7.95), 'STEAK':(6.50, 7.95),
            'STEAK_CHEESE':(6.95, 8.50), 'STEAK_GPEPPERS':(7.45, 9.00), 
            'STEAK_MUSHROOMS':(7.45, 9.00), 'STEAK_ONIONS':(7.45, 9.00), 
            'TUNA':(6.50, 7.95), 'TURKEY':(7.50, 8.50),
            'VEGGIE':(6.95, 8.50), 'SAPEON':(0, 8.50),
            'XCHEESE':(0.50, 0.50)
        }
        self.pasta = {
            'BZ MOZZARELA': 6.50,
            'BZ MEATBALLS': 8.75,
            'BZ CHICKEN': 9.75
        }
        self.salad = {
            'GARDEN': 6.25,
            'GREEK': 8.25,
            'ANTIPASTO': 8.25,
            'TUNA': 8.25
        }
        self.dinner = {
            'GARDEN SALAD': (35.00, 60.00),
            'GREEK SALAD': (45.00, 70.00),
            'ANTIPASTO': (45.00, 70.00),
            'BAKED ZITI': (35.00, 60.00),
            'MEAT PARM': (45.00, 70.00),
            'CHICKEN PARM': (45.00, 80.00)
        }

    def getRegular(self, p):
        return self.regular.get(p)
    
    def getSicilian(self, p):
        return self.sicilian.get(p)

    def getSub(self, p):
        return self.sub.get(p)
    
    def getPasta(self, p):
        return self.pasta.get(p)

    def getSalad(self, p):
        return self.salad.get(p)

    def getDinner(self, p):
        return self.dinner.get(p)