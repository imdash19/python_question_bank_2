# Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model} engine has started!")


make = input()
model = input()
year = int(input())

car = Car(make, model, year)
car.start_engine()
