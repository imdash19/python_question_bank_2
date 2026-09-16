# Employee Salary System
# Problem Statement
# Create a program to manage an employee's salary information securely. The salary should be stored privately so that no one can access or change it directly from outside. When creating an employee record, the program should accept a salary value from the user. However, there's a safety rule: if someone accidentally enters a negative salary (which doesn't make sense in real life), the system should automatically correct it to 0 instead of storing an invalid value.
# After creating the employee record, display the salary using a special method that allows controlled access to view the salary without exposing it directly.
# Input Format:

# A single number representing the employee's salary

# Output Format:
# A message displaying the employee's salary

class Employee:
    def __init__(self, salary):
        if salary < 0:
            salary= 0
        self.__salary= salary

    def get_salary(self):
        return f'Employee Salary: {self.__salary}'

e= Employee(float(input()))
print(e.get_salary())
