# Alex Rapp
# UWYO COSC 1010
# 11/12/2024
# Lab 09
# Lab Section: 11
# Sources, people worked with, help given to:
# lecture notes, previos assignments
# N/a
# N/a

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
class pizza:
    def __init__(self, size, sauce='red'):
        self.size = self.sizelimit(size)
        self.toppings = ['cheese']
        self.sauce = self.saucecheck()

    def toppingcheck(self):
        toppings=['cheese']
        return self.toppings
    def saucecheck(self,sauce=''):
        if sauce != '':
            return sauce
        else:
            return 'red'
    def sizelimit(self, size):
        if str(size).isdigit():
            if int(size) > 10:
                return int(size)
            else:
                return 10
        else:
            return 10
    def addtopping(self, *args):
        for topping in args:
            self.toppings.append(topping)
    def amounttop(self):
        return len(self.toppings)
    def getSize(self):
        return self.size
            
        

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.
class pizzaria:
    def __init__(self):
        self.orders = 0
        self.price_per_topping = .3
        self.price_per_inch = .6
        self.pizzas = []

    def placeOrder(self,size=0,sauze=''):
        self.orders += 1
        new_pizza = pizza(0,0)
        size =  input('what size would you like your pizza to be?')
        if size.isdigit():
            if int(size) > 0:
                size = int(size)
            else:
                size= 10
        else:
            new_pizza.size = 10
        sauce = input('what sauce would you like?\nif nothing is entered the sauce will be red.')
        if sauce != '':
            sauce = sauce
        else:
            sauce = 'red'
        new_pizza = pizza(size,sauce)
        toppings = input('what toppings would you like? \nentered with a space inbetween each topping')
        if toppings != '':
            new_pizza.addtopping(*toppings.split())
        self.pizzas.append(new_pizza)
        return new_pizza
    def getPrice(self,price=0):
        price =  (pizza.sizelimit() * self.price_per_inch) + pizza.amounttop() * self.price_per_topping
        return price
    def getReceipt(self,pizza):
        sipri = pizza.getSize()* self.price_per_inch
        toppri = pizza.amounttop() * self.price_per_topping
        totpri = sipri  + toppri
        print(f'your sauce is {pizza.sauce}\nyour size is {pizza.size} inches\nyour toppings are {pizza.toppings[:]}\nthe price for that size is {sipri} dollars\nthe price for those toppings is {toppri} dollars\nThe total price for the pizza is {totpri} dollars')
    def getNumberOfOrders(self):
        return self.orders

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
pizzaz = pizzaria()
user = input('would you like to place an order?\nenter "exit" if not')
while True:
    while user.lower() != 'exit':
        npizza = pizzaz.placeOrder()
        pizzaz.getReceipt(npizza)
        user = input('would you like to place another order?\nenter "exit" if not')
    print(f'you ordered {pizzaz.getNumberOfOrders()} pizzas.')
    break

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""
