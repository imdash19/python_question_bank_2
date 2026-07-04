# Write a program to demonstrate the difference between class variables and instance variables in Python.

# Description

# Create an Employee class with:
# Class variable company = "ABC Corp"
# Instance variable name (provided during object creation)
# Print both the class and instance variables using the object

class Emplyee:
    company= 'ABC Corp'
    def __init__(self, name):
        self.name= name
        

e= Emplyee(input())
print(f'Company: {e.company} Name: {e.name}')
