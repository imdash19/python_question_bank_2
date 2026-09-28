# Base class Employee: method get_basic_salary() to store/retrieve salary.
# Child class Developer: calculates salary by adding 20% bonus.

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_basic_salary(self):
        return self.salary


class Developer(Employee):
    def calculate_salary(self):
        basic_salary = self.get_basic_salary()
        bonus = basic_salary * 20 / 100
        return basic_salary + bonus


salary = float(input())

developer = Developer(salary)

print(developer.calculate_salary())
