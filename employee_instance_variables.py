# Create a class Employee. Define instance variables name and salary inside the constructor. 
# Accept inputs and print both values.

classs Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary

e= Employee(input(), int(input()))
print(e.name, e.salary)
