# Create a class Salary with attribute amount. 
# Overload the + operator using __add__() to calculate total salary of two employees.

class Salary:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Salary(self.amount + other.amount)


salary1 = float(input())
salary2 = float(input())

employee1 = Salary(salary1)
employee2 = Salary(salary2)

total_salary = employee1 + employee2

print(total_salary.amount)
