# Create a class Area with method calculate_area(). 
# If one argument is passed calculate area of square. 
# If two arguments are passed calculate area of rectangle.

class Area:
    def calculate_area(self, length, width= None):
        if width is not None:
            return length * width
        else:
            return length * length

values= list(map(int, input().split()))

a= Area()
if len(values) == 1:
    print(a.calculate_area(values[0]))
elif len(values) == 2:
    print(a.calculate_area(values[0], values[1]))
