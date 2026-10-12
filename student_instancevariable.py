# Problem Statement
# Write a program to demonstrate the use of instance variables in Python.
# Description
# Create a Student class with a constructor that accepts the student’s name.
# Store the name as an instance variable.
# Print the name using the object.

class Student:
    def __init__(self, name):
        self.name= name

print(f'Student Name: {Student(input()).name}')
