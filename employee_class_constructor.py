# Write a Python program to define a class named Employee with attributes emp_id, name, and salary.
# Accept employee details from the user through console input.
# Use a constructor to initialize the attributes.
# Create an object of the Employee class using the entered values.
# Access all attributes using dot notation. 
# Display employee details clearly in the output.

class Employee:
    def __init__(self, eid, name, salary):
        self.eid= eid
        self.name= name
        self.salary= salary

eid= int(input())
name= input()
salary= int(input())

e= Employee(eid, name, salary)

print(f'''ID : {e.eid}
Name : {e.name}
Salary : {e.salary}''')
