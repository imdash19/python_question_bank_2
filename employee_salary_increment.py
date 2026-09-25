# Create a class Employee with a public attribute salary. 
# Read the salary from the user. Increase the salary by 10 percent and print the updated salary using the object.

class Employee:
    def __init__(self, salary):
        self.salary= salary + salary * 0.10 

e= Employee(int(input()))
print(int(e.salary))
