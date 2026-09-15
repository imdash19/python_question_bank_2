# Write a Python program to create a class Product with class variable category = "Electronics" 
# and instance variables name and price. 
# Accept product details from the user. 
# Create product objects and display product name, price, and category.
# Show that category remains common while product details differ.

class Product:
    category = "Electronics"
    def __init__(self, name, price):
        self.name= name
        self.price= price

p= Product(input(), int(input()))
print(f'''{p.name}
{p.price}
{p.category}''')
