# This program demonstrates how a child class can access parent class methods using single inheritance.

# Create a parent class Vehicle with a method show_speed() that prints the speed.
# Create a child class Bike that inherits from Vehicle.
# Read speed from the user.

# Create a Bike object and call show_speed() using the child object.

class Vehicle:
    def __init__(self, speed):
        self.speed= speed

    def show_speed(self):
        return self.speed

class Bike(Vehicle):
    pass

print(f'Speed: {Bike(int(input())).show_speed()}')
