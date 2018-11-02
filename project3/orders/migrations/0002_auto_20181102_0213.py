# Generated by Django 2.1.2 on 2018-11-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatters',
            name='dinner',
            field=models.CharField(blank=True, choices=[('G1', 'Garden Salad'), ('G2', 'Greek Salad'), ('AP', 'Antipasto'), ('BZ', 'Baked Ziti'), ('MP', 'Meatball Parm'), ('CP', 'Chicken Parm')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='dinnerplatters',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('L', 'Large')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='pasta',
            field=models.CharField(blank=True, choices=[('M2', 'Baked Ziti w/ Mozzarella'), ('M1', 'Baked Ziti w/ Meatballs'), ('C1', 'Baked Ziti w/ Chicken')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salad',
            name='salad',
            field=models.CharField(blank=True, choices=[('G1', 'Garden Salad'), ('G2', 'Greek Salad'), ('AP', 'Antipasto'), ('ST', 'Salad w/ Tuna')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('L', 'Large')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='subs',
            field=models.CharField(blank=True, choices=[('C1', 'Cheese'), ('C2', 'Cheeseburger'), ('C3', 'Chicken Parmigiana'), ('E1', 'Eggplant Parmigiana'), ('E2', 'Extra Cheese on any subs'), ('F1', 'Fried Chicken'), ('H1', 'Ham + Cheese'), ('H2', 'Hamburger'), ('I1', 'Italian'), ('M1', 'Meatball'), ('S1', 'Sausage, Peppers & Onions'), ('S2', 'Steak'), ('S3', 'Steak + Cheese'), ('S4', 'Steak + Green Peppers'), ('S5', 'Steak + Mushrooms'), ('S6', 'Steak + Onions'), ('T1', 'Tuna'), ('T2', 'Turkey'), ('V1', 'Veggie')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='topping',
            field=models.CharField(blank=True, choices=[('A1', 'Anchovies'), ('A2', 'Artichoke'), ('B1', 'Barbecue Chicken'), ('B2', 'Black Olives'), ('B3', 'Buffalo Chicken'), ('C1', 'Canadian Bacon'), ('E1', 'Eggplant'), ('F1', 'Fresh Garlic'), ('G1', 'Green Peppers'), ('H1', 'Ham'), ('H2', 'Hamburger'), ('M1', 'Mushrooms'), ('O1', 'Onions'), ('P1', 'Pepperoni'), ('P2', 'Pineapple'), ('S1', 'Sausage'), ('S2', 'Spinach'), ('T1', 'Tomato & Basil'), ('Z1', 'Zucchini')], max_length=2, null=True),
        ),
    ]