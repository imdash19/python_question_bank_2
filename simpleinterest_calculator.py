# Write a program that finds the quotient and remainder when dividing two numbers. The program takes two inputs: the dividend (number to be divided) and the divisor (number to divide by). Each input should be taken on a separate line. Use Python's divmod() function to calculate both quotient and remainder in a single operation and display them on separate lines.
# Input Format: Two lines containing the dividend and divisor as integers.
# Output Format: Two lines showing the quotient on the first line and remainder on the second line.

principal = float(input())
rate = float(input())
time = float(input())

simple_interest = (principal * rate * time) / 100

print(simple_interest)
