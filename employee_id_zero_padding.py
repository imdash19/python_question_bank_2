# You are building an employee ID card generation system for a company. The company wants all employee IDs to have a fixed length with leading zeros to maintain a uniform format.Here's how it works:

# Every employee gets a unique ID number (like 5, 42, 158)
# All IDs must be displayed with the same total width (number of digits)
# If an ID has fewer digits than the required width, add zeros at the beginning
# This creates a professional, uniform look for all employee IDs
# Example 1: Employee number = 42, Width = 6
# Output: "000042"Example 2: Employee number = 1234, Width = 6
# Output: "001234"You need to create a program that:

# Takes an employee number as input
# Takes the required ID width (total digits) as input
# Displays the employee ID with leading zeros to match the width using .format() method
# Input Format:

# First line: Employee number (integer)
# Second line: Required ID width (integer)
# Output Format:

# Print the formatted employee ID with leading zeros

employee_number = int(input())
width = int(input())

employee_id = "{:0{}}".format(employee_number, width)

print(employee_id)
