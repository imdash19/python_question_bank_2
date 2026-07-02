# Create an Employee class with a protected attribute _salary.
# Use a method to print:
# "High Salary" if _salary > 30000
# "Normal Salary" if _salary ≤ 30000

class Employee:
    def __init__(self, salary):
        self._salary= salary

e= Employee(int(input()))

if e._salary > 30000:
    print('High Salary')
else:
    print('Normal Salary')
