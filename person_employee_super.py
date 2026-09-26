# Create a parent class Person
# Method: show_name()
# Create a child class Employee(Person)
# Method: display()
# Inside display(), call:
# super().show_name()
# Take name from input and print it.

class Person:
    def __init__(self, name):
        self.name= name
    
    def show_name(self):
        return self.name

class Employee(Person):
    def display(self):
        return super().show_name()

e= Employee(input())
print(e.display())
