# Write a Python program to define a class named Flight. 
# The class should contain attributes flight_no, origin, destination, and duration. 
# The program must accept flight details from the user through console input. 
# Use a constructor to initialize all attributes with the entered values. 
# Create an object of the Flight class using the user-provided data.
# Access each attribute using dot notation. Display all flight details clearly in the output.

class Flight:
    def __init__(self, flight_no, origin, destination, duration):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.duration = duration


flight_no = input()
origin = input()
destination = input()
duration = input()

flight = Flight(flight_no, origin, destination, duration)

print("Flight No:", flight.flight_no)
print("Origin:", flight.origin)
print("Destination:", flight.destination)
print("Duration:", flight.duration)
