# Write a Python program to define a class named Car with attributes make, model, and year.
# Accept car details from the user using console input. 
# Use a constructor to initialize the attributes. 
# Create an object of the Car class using the entered values. 
# Access all attributes using dot notation. 
# Display the car details clearly in the output.

class Car:
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year= year

make= input()
model= input()
year= int(input())
c= Car(make, model, year)
print(f'''Make : {c.make}
Model: {c.model}
Year : {c.year}''')
