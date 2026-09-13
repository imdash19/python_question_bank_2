# Write a Python program to define a class Point with attributes x and y.
# Accept coordinates of two points from the user. Create two objects p1 and p2. 
# Print coordinates of both points using object references. 
# This is useful in graphics and geometric computations.

class Point:
    def __init__(self, x, y):
        self.x= x
        self.y= y

x1= int(input())
y1= int(input())
x2= int(input())
y2= int(input())

p1= Point(x1, y1)
p2= Point(x2, y2)

print(f'''Point1: ({p1.x},{p1.y})
Point2: ({p2.x},{p2.y})''')
