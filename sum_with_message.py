# Write a Python program that takes two numbers from the user, adds them together, and displays the result with a clear message. Use the print() function with commas to show both the message and the sum in a single line.
# For example, if the user enters "15" and "25", your program should calculate 15 + 25 = 40 and display "The sum is 40" (message and result in one line).
# Input Format:
# Two separate lines, each containing one integer number
# Output Format:
# A message followed by the sum, displayed in one line (e.g., "The sum is 40")

n1, n2= int(input()), int(input())
print(f'The sum is{n1+n2}')
