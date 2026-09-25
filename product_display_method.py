# Create a class Product with a public method display(). 
# Accept product name from the user and print it using the display method.

class Product:
    def __init__(self, prod):
        self.prod= prod

    def display(self):
        return self.prod

p= Product(input())
print(f'Product: {p.display()}')
