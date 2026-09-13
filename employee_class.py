# Write a Python program to define a class named Employee. 
# The class should store employee id and department name. 
# Accept input values from the user through the console. 
# Create an object of the class. Display employee details using instance variables. 
# Ensure proper usage of self keyword for attribute access.

class Employee:
    def __init__(self, eid, dept):
        self.eid= eid
        self.dept= dept

    def display(self):
        return f'''ID: {self.eid}
        Dept: {self.dept}'''

e= Employee(int(input()), input())
print(e.display())
