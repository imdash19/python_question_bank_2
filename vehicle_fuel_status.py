# Write a program to demonstrate inheritance using a parent and child class to check the fuel status of a vehicle.

# Description

# Create a parent class Vehicle with a fuel attribute.
# Create a child class that inherits from the Vehicle class.
# Use the super() method to pass the fuel value to the parent class constructor.
# Based on the fuel level, display the vehicle’s fuel status.

# Fuel Conditions

# If fuel is less than 10 liters, print “Refuel Needed”
# If fuel is 10 liters or more, print “Ready to Go”

class Vehicle:
    def __init__(self, fuel):
        self.fuel= fuel

class Car(Vehicle):
    def __init__(self, fuel):
        super().__init__(fuel)

    def check_status(self):
        if self.fuel >= 10:
            return 'Ready to Go'
        
        else:
            return 'Refuel Needed'

c= Car(int(input()))
print(c.check_status())
