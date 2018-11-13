from .models import Order

class Prices:
    '''Prices for pizzas and its additions'''

    def __init__(self):
        self.cost = {}
        self.total = None

    # dict = {type: (price for small", "price for large)}
    regular = {
        'CHEESE':("12.20", "17.45"),
        'SPECIAL':("17.25", "25.45"),
        '1':("13.20", "19.45"),
        '2':("14.70", "21.45"),
        '3':("15.70", "23.45")
    }
    sicilian = {
        'CHEESE':("23.45", "37.70"),
        '1 TOPPINGS':("25.45", "39.70"),
        '2 TOPPINGS':("27.45", "41.70"),
        '3 TOPPINGS':("28.45", "43.70"),
        'SPECIAL':("29.45", "44.70")
    }
    sub = {
        'CHEESE':("6.50", "7.95", 'Cheese'),
        'CHEESEBURGER':("5.10", "7.45", 'Cheeseburger'),
        'CHICKEN PARM':("7.50", "8.50", 'Chicken Parmigiana'),
        'EGGPLANT PARM':("6.50", "7.95", 'Eggplant Parmigiana'),
        'FRIED CHICKEN':("6.95", "8.50", 'Fried Chicken'),
        'HAM_CHEESE':("6.50", "7.95", 'Ham + Cheese'),
        'HAMBURGER':("4.60", "6.95", 'Hamburger'),
        'ITALIAN':("6.50", "7.95", 'Italian'),
        'MEATBALL':("6.50", "7.95", 'Meatball'),
        'SAPEON':(None, "8.50", 'Sausage, Peppers & Onions'),
        'STEAK':("6.50", "7.95", 'Steak'),
        'STEAK_CHEESE':("6.95", "8.50", 'Steak + Cheese'),
        'STEAK_GPEPPERS':("7.45", "9.00", 'Steak + Green Peppers'),
        'STEAK_MUSHROOMS':("7.45", "9.00", 'Steak + Mushrooms'),
        'STEAK_ONIONS':("7.45", "9.00", 'Steak + Onions'),
        'TUNA':("6.50", "7.95", 'Tuna'),
        'TURKEY':("7.50", "8.50", 'Turkey'),
        'VEGGIE':("6.95", "8.50", 'Veggie'),
        'XCHEESE':("0.50", "0.50", 'Extra Cheese on any subs')
    }
    pasta = {
        'BZ MOZZARELLA': ("6.50", 'Baked Ziti w/ Mozzarella'),
        'BZ MEATBALLS': ("8.75", 'Baked Ziti w/ Meatballs'),
        'BZ CHICKEN': ("9.75", 'Baked Ziti w/ Chicken')
    }
    salad = {
        'GARDEN': ("6.25", 'Garden Salad'),
        'GREEK': ("8.25", 'Greek Salad'),
        'ANTIPASTO': ("8.25", 'Antipasto'),
        'TUNA': ("8.25", 'Salad w/ Tuna')
    }
    dinner = {
        'GARDEN SALAD': ("35.00", "60.00", 'Garden Salad'),
        'GREEK SALAD': ("45.00", "70.00", 'Greek Salad'),
        'ANTIPASTO': ("45.00", "70.00", 'Antipasto'),
        'BAKED ZITI': ("35.00", "60.00", 'Baked Ziti'),
        'MEAT PARM': ("45.00", "70.00", 'Meatball Parm'),
        'CHICKEN PARM': ("45.00", "80.00", 'Chicken Parm')
    }

    def get_items_prices(self, ob):
        '''Group each item's price
        '''
        # Store toppings
        t = ob.pizza.toppings_options

        if ob.pizza.pizzas == "REG":
            if ob.pizza.pizza_size == "S": # for SMALL
                self.cost['Small Regular'] = self.regular[t][0]
            
            else: # for LARGE
                self.cost['Large Regular'] = self.regular[t][1]

        else: # for SICILIAN
            if ob.pizza.pizza_size == "S":
                self.cost['Small Sicilian'] = self.sicilian[t][0]
            else:
                self.cost['Large Sicilian'] = self.sicilian[t][1]

        if ob.sub is not None:

            if ob.sub.sub_size == "S":
                self.cost['Small Sub'] = self.sub[ob.sub.subs][0]
            else:
                self.cost['Large Sub'] = self.sub[ob.sub.subs][1]
        
        if ob.pasta is not None:
            self.cost['Pasta'] = self.pasta[ob.pasta.pastas][0]
        
        if ob.salad is not None:
            self.cost['Salad'] = self.salad[ob.salad.salads][0]

        if ob.dinner is not None:

            if ob.dinner.dinner_size == "S":
                self.cost['Small Dinner'] = self.dinner[ob.dinner.dinners][0]
            else:
                self.cost['Large Dinner'] = self.dinner[ob.dinner.dinners][1]
        
        return self.cost
        
    
    def get_total(self, ob):
        '''Calculate total order cost
            Return a dict of tuple (int:total, dict:items w/ price)
        '''
        self.get_items_prices(ob)
        nums_list = [float(e) for e in self.cost.values()]
        self.total = round(sum(nums_list), 2)
        return self.total

