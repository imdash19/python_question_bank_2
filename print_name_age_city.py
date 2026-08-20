# Write a Python program that takes three pieces of information from the user: their name, age, and city. Store each piece in a separate variable. Then, use the print() function with commas to display all three values in a single line. When you use commas in the print function, Python automatically adds spaces between the values.
# For example, if the user enters "Rahul", "22", and "Mumbai", your program should display them as "Rahul 22 Mumbai" (all in one line with spaces between them).
# Input Format:
# Three separate lines:

# First line: Name (text)
# Second line: Age (number)
# Third line: City (text)

# Output Format:
# All three values displayed in a single line, separated by spaces

name = input()
age = int(input())
city = input()

print(name, age, city)
