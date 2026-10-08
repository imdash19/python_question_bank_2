# Create an Employee class with attributes emp_id and emp_name then create an object and display values

class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name


emp_id = int(input())
emp_name = input()

employee = Employee(emp_id, emp_name)

print(employee.emp_id)
print(employee.emp_name)
