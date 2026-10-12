# Write a program to demonstrate the use of a class variable to count the number of objects created from a class.

# Description
# Create a Student class with a class variable count initialized to 0.
# Increment count in the constructor whenever a new object is created.
# Print the total number of objects created

class Student:
    cnt= 0
    def __init__(self):
        Student.cnt+= 1

s1= Student()
s2= Student()
print(f'Total Objects: {s2.cnt}')
