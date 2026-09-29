# Create a class SalaryCalculator with method calculate_salary(). 
# If only basic salary is passed print basic salary. 
# If basic salary and bonus are passed calculate and print total salary.

class SalaryCalculator:
    def calculate_salary(self, basic_salary, bonus=0):
        return basic_salary + bonus


values = list(map(float, input().split()))

calculator = SalaryCalculator()

if len(values) == 1:
    print(f"{calculator.calculate_salary(values[0]):.2f}")
elif len(values) == 2:
    print(f"{calculator.calculate_salary(values[0], values[1]):.2f}")
