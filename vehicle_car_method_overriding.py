# Create a parent class Vehicle with method show_speed(speed). 
# Create a child class Car that overrides show_speed() to print speed with message Car Speed.
# Car Speed: <speed>

class Vehicle:
    def show_speed(self, speed):
        print(speed)

class Car(Vehicle):
    def show_speed(self, speed):
        print(f'Car Speed: {speed}')

Car().show_speed(int(input()))
