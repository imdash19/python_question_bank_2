# You need to create a program that calculates bonuses for employees based on their job type and salary.
# There are two types of employees:

# Manager: Gets a bonus of 10% of salary if their salary is more than 30,000. Otherwise, no bonus.
# Clerk: Gets a bonus of 5% of salary if their salary is more than 20,000. Otherwise, no bonus.

# Input Format:

# First line: Employee type (either "Manager" or "Clerk")
# Second line: Employee salary (a number)

# Output Format:

# Print the bonus amount (rounded to 2 decimal places)

class Employee:
    def get_salary(self, salary):
        self.salary = salary


class Manager(Employee):
    def calculate_bonus(self):
        if self.salary > 30000:
            return self.salary * 0.10
        return 0.0


class Clerk(Employee):
    def calculate_bonus(self):
        if self.salary > 20000:
            return self.salary * 0.05
        return 0.0


emp_type = input()
salary = float(input())

if emp_type == "Manager":
    emp = Manager()
else:
    emp = Clerk()

emp.get_salary(salary)
print(f"{emp.calculate_bonus():.2f}")
