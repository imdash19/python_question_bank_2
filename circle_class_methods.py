# Write a Python program to define a class Circle with attribute radius. 
# Add a method area() to calculate the area of the circle.
# Add a method perimeter() to calculate the perimeter of the circle.
# Accept radius input from the user. Create a Circle object with the given radius. 
# Call the area() and perimeter() methods and display the results. 
# Round the outputs to two decimal places.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


radius = float(input())

circle = Circle(radius)

print("Area:", round(circle.area(), 2))
print("Perimeter:", round(circle.perimeter(), 2))
