from django import forms
from django.forms import ModelForm
from .models import *

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'

class ToppingForm1(ModelForm):
    class Meta:
        model = Topping1
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ToppingForm1, self).__init__(*args, **kwargs)
        self.fields['toppings'].widget.attrs.update({
            'class': 'topping1',
        })

class ToppingForm2(ModelForm):
    class Meta:
        model = Topping2
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ToppingForm2, self).__init__(*args, **kwargs)
        self.fields['toppings'].widget.attrs.update({
            'class': 'topping2',
        })

class ToppingForm3(ModelForm):
    class Meta:
        model = Topping3
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ToppingForm3, self).__init__(*args, **kwargs)
        self.fields['toppings'].widget.attrs.update({
            'class': 'topping3',
        })

class SubForm(ModelForm):
    class Meta:
        model = Sub
        fields = '__all__'

class PastaForm(ModelForm):
    class Meta:
        model = Pasta
        fields = '__all__'

class SaladForm(ModelForm):
    class Meta:
        model = Salad
        fields = '__all__'

class DinnerPlatterForm(ModelForm):
    class Meta:
        model = DinnerPlatter
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

