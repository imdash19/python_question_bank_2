# Design a program using Multilevel Inheritance.

# Create a base class Person with method get_name().
# Create a child class Employee that inherits Person and has method get_basic_salary().
# Create another child class SalaryDetails that inherits Employee and calculates total salary by adding 20% HRA using calculate_salary() method.

class Person:
    def __init__(self, name):
        self.name= name

    def get_name(self):
        return self.name

class Employee(Person):
    def __init__(self, salary):
        self.salary= salary

    def get_basic_salary(self):
        return self.salary

class SalaryDetails(Employee):
    def calculate_salary(self):
        basic_salary= super().get_basic_salary()
        hra= (basic_salary) * 0.20
        return int(basic_salary + hra)

name, salary= input().split()
print(SalaryDetails(int(salary)).calculate_salary())
