# Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.

employees = [
    {"name": "Rahul", "salary": 30000},
    {"name": "Priya", "salary": 45000},
    {"name": "Amit", "salary": 25000},
    {"name": "Sneha", "salary": 50000}
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

for employee in sorted_employees:
    print(employee)
