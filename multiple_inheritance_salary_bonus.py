# Write a Python program to calculate the total salary of an employee using Multiple Inheritance. You need to implement three classes: Salary, Bonus, and Employee. The total salary includes a 10% bonus, but this bonus is only applicable if the employee's basic salary is greater than 10,000.

class Salary:
    def get_salary(self, basic_salary):
        return basic_salary


class Bonus:
    def get_bonus(self, basic_salary):
        if basic_salary > 10000:
            return basic_salary * 10 / 100
        return 0


class Employee(Salary, Bonus):
    def total_salary(self, basic_salary):
        salary = self.get_salary(basic_salary)
        bonus = self.get_bonus(basic_salary)
        return salary + bonus


basic_salary = float(input())

employee = Employee()

print(employee.total_salary(basic_salary))
