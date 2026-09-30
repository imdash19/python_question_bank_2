# Create a class Distance with attribute meters. 
# Overload the + operator using __add__() to add two Distance objects and print the total distance.

class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)


meters1 = int(input())
meters2 = int(input())

distance1 = Distance(meters1)
distance2 = Distance(meters2)

total = distance1 + distance2

print(total.meters)
