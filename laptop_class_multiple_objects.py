# Write a Python program to define a class named Laptop. 
# The class should contain attributes brand, model, and price. 
# The program must accept laptop details from the user through console input. 
# Create multiple objects of the Laptop class using different user inputs. 
# Store the details for each laptop using a constructor.
# Access all attributes using dot notation. 
# Display the details of each laptop clearly in the output.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


brand1 = input()
model1 = input()
price1 = float(input())

brand2 = input()
model2 = input()
price2 = float(input())

laptop1 = Laptop(brand1, model1, price1)
laptop2 = Laptop(brand2, model2, price2)

print("Laptop 1:")
print("Brand:", laptop1.brand)
print("Model:", laptop1.model)
print("Price:", laptop1.price)

print("Laptop 2:")
print("Brand:", laptop2.brand)
print("Model:", laptop2.model)
print("Price:", laptop2.price)
