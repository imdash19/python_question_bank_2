# This program demonstrates single inheritance in Python.
# Create a parent class Person with a method display_name() that prints the name.
# Create a child class Employee that inherits from Person.
# Accept the employee name from the user.

# Create an Employee object and call display_name() using the child object.

class Person:
    def __init__(self, name):
        self.name= name

    def display_name(self):
        return self.name

class Employee(Person):
    def display_employee(self):
        return super().display_name()

print(Employee(input()).display_name())
