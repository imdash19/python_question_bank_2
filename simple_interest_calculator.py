# Write a program that calculates simple interest based on user input. The program takes three inputs: principal amount, rate of interest per year, and time period in years. Each input should be taken on a separate line. Calculate the simple interest using the formula SI = (P * R * T)/100 and display the result as a decimal number.
# Input Format: Three lines containing principal amount, rate of interest, and time in years respectively.
# Output Format: A single line showing the calculated simple interest value.

principal = float(input())
rate = float(input())
time = float(input())

simple_interest = (principal * rate * time) / 100

print(simple_interest)
