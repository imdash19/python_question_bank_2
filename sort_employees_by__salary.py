# Given a list of tuples representing employees (Name, Age, Salary), sort the list primarily by Salary in descending order.

employees = [
    ("Rahul", 25, 30000),
    ("Priya", 28, 45000),
    ("Amit", 24, 25000),
    ("Sneha", 27, 50000)
]

sorted_employees = sorted(employees, key=lambda employee: employee[2], reverse=True)

for employee in sorted_employees:
    print(employee)
