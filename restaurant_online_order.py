# This program demonstrates single inheritance in Python.
# Create a parent class Restaurant with a method show_menu() that prints a static message.
# Create a child class OnlineOrder that inherits from Restaurant.
# Create an OnlineOrder object and call the show_menu() method using the child object.

class Resturant:
    def show_menu(self):
        return 'Menu Displayed'

class OnlineOrder(Resturant):
    pass

print(OnlineOrder().show_menu)
