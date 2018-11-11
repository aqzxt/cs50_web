class Prices:
    '''Prices for pizzas and its additions'''
    # dict = {type: (price for small", "price for large)}
    regular = {
        'CHEESE':("12.20", "17.45"),
        '1 TOPPINGS':("13.20", "19.45"),
        '2 TOPPINGS':("14.70", "21.45"),
        '3 TOPPINGS':("15.70", "23.45"),
        'SPECIAL':("17.25", "25.45")
    }
    sicilian = {
        'CHEESE':("23.45", "37.70"),
        '1 TOPPINGS':("25.45", "39.70"),
        '2 TOPPINGS':("27.45", "41.70"),
        '3 TOPPINGS':("28.45", "43.70"),
        'SPECIAL':("29.45", "44.70")
    }
    sub = {
        'CHEESE':("6.50", "7.95"), 'CHEESEBURGER':("5.10", "7.45"),
        'CHICKEN PARM':("7.50", "8.50"), 'EGGPLANT PARM':("6.50", "7.95"),
        'FRIED CHICKEN':("6.95", "8.50"), 'HAM_CHEESE':("6.50", "7.95"),
        'HAMBURGER':("4.60", "6.95"), 'ITALIAN':("6.50", "7.95"),
        'MEATBALL':("6.50", "7.95"), 'STEAK':("6.50", "7.95"),
        'STEAK_CHEESE':("6.95", "8.50"), 'STEAK_GPEPPERS':("7.45", "9.00"),
        'STEAK_MUSHROOMS':("7.45", "9.00"), 'STEAK_ONIONS':("7.45", "9.00"),
        'TUNA':("6.50", "7.95"), 'TURKEY':("7.50", "8.50"),
        'VEGGIE':("6.95", "8.50"), 'SAPEON':("0", "8.50"),
        'XCHEESE':("0.50", "0.50")
    }
    pasta = {
        'BZ MOZZARELA': "6.50",
        'BZ MEATBALLS': "8.75",
        'BZ CHICKEN': "9.75"
    }
    salad = {
        'GARDEN': "6.25",
        'GREEK': "8.25",
        'ANTIPASTO': "8.25",
        'TUNA': "8.25"
    }
    dinner = {
        'GARDEN SALAD': ("35.00", "60.00"),
        'GREEK SALAD': ("45.00", "70.00"),
        'ANTIPASTO': ("45.00", "70.00"),
        'BAKED ZITI': ("35.00", "60.00"),
        'MEAT PARM': ("45.00", "70.00"),
        'CHICKEN PARM': ("45.00", "80.00")
    }
