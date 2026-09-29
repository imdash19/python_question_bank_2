# You need to create a program that calculates the total salary of an employee by adding a bonus to their basic salary.
# The program should:

# Take an employee's name and basic salary as input
# Calculate a bonus which is 10% of the basic salary
# Add the bonus to the basic salary to get the total salary

# Input Format:

# First line: Employee name (a string)
# Second line: Basic salary (a number)

# Output Format:

# Print the total salary including bonus (rounded to 2 decimal places)

name= input()
salary= float(input())
bonus= salary * 0.10
print(f'{salary+bonus:.2f}')
