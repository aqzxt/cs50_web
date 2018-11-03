from django.db import models

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
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return f"{self.size} {self.type} Pizza"

class Topping(models.Model):
    '''Represents a topping addition. Default value is NULL'''
    TOPPINGS = (
        ('ANCHOVY', 'Anchovies'), ('ARTICHOKE', 'Artichoke'), 
        ('BACHICKEN', 'Barbecue Chicken'), ('BOLIVE', 'Black Olives'), 
        ('BUCHICKEN', 'Buffalo Chicken'), ('CBACON', 'Canadian Bacon'), 
        ('EGGPLANT', 'Eggplant'), ('FGARLIC', 'Fresh Garlic'), 
        ('GPEPPER', 'Green Peppers'), ('HAM', 'Ham'), 
        ('HAMBURGER', 'Hamburger'), ('MUSHROOM', 'Mushrooms'), 
        ('ONION', 'Onions'), ('PEPPERONI', 'Pepperoni'), 
        ('PINEAPPLE', 'Pineapple'), ('SAUSAGE', 'Sausage'), 
        ('SPINACH', 'Spinach'), ('TOMATOBASIL', 'Tomato & Basil'), 
        ('ZUCCHINI', 'Zucchini')
    )
    topping = models.CharField(max_length=20, null=True, blank=True, choices=TOPPINGS)

    def __str__(self):
        return f"{self.topping} Topping"
    

class Sub(models.Model):
    '''Represents a submarine sandwich addition. Default value is NULL'''
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    SUBS = (
        ('CHEESE', 'Cheese'), ('CHEESEB', 'Cheeseburger'), 
        ('CHICKEN', 'Chicken Parmigiana'), ('EGGPLANT', 'Eggplant Parmigiana'), 
        ('XCHEESE', 'Extra Cheese on any subs'), ('FCHICKEN', 'Fried Chicken'), 
        ('HAMC', 'Ham + Cheese'), ('HAMBURGER', 'Hamburger'), 
        ('ITALIAN', 'Italian'), ('MEAT', 'Meatball'), 
        ('SAPEON', 'Sausage, Peppers & Onions'), ('STEAK', 'Steak'), 
        ('STEAKC', 'Steak + Cheese'), ('STEAKG', 'Steak + Green Peppers'), 
        ('STEAKM', 'Steak + Mushrooms'), ('STEAKO', 'Steak + Onions'), 
        ('TUNA', 'Tuna'), ('TURKEY', 'Turkey'), ('VEGGIE', 'Veggie')
    )
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)
    sub = models.CharField(max_length=20, null=True, blank=True, choices=SUBS)

    def __str__(self):
        return f"{self.size} {self.subs} Subs"

class Pasta(models.Model):
    '''Represents a pasta addition. Default value is NULL'''
    PASTA = (
        ('MOZZA', 'Baked Ziti w/ Mozzarella'),
        ('MEAT', 'Baked Ziti w/ Meatballs'),
        ('CHICKEN', 'Baked Ziti w/ Chicken')
    )
    pasta = models.CharField(max_length=20, null=True, blank=True, choices=PASTA)

    def __str__(self):
        return f"{self.pasta} Pasta"

class Salad(models.Model):
    '''Represents a salad addition. Default value is NULL'''
    SALADS = (
        ('GARDEN','Garden Salad'),
        ('GREEK', 'Greek Salad'),
        ('APASTO', 'Antipasto'),
        ('TUNA', 'Salad w/ Tuna')
    )
    salad = models.CharField(max_length=20, null=True, blank=True, choices=SALADS)

    def __str__(self):
        return f"{self.salad} Salad"

class DinnerPlatter(models.Model):
    '''Represents a dinner platter addition. Default value is NULL'''
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    DINNER = (
        ('GARDEN','Garden Salad'),
        ('GREEK', 'Greek Salad'),
        ('APASTO', 'Antipasto'),
        ('ZITI', 'Baked Ziti'),
        ('MEAT', 'Meatball Parm'),
        ('CHICKEN', 'Chicken Parm')
    )
    size = models.CharField(max_length=1, null=True, blank=True, choices=SIZES)
    type = models.CharField(max_length=20, null=True, blank=True, choices=DINNER)

    def __str__(self):
        return f"{self.size} {self.dinner} Dinner Platter"

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
        
        return f"({self.id}) {self.pizza}{t}{su}{p}{sa}{d}"