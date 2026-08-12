# Write a Python program to determine the interest rate based on age and income.
# Two integers: age, income
# "Interest Rate: 8%" if age > 60
# "Interest Rate: 7%" if income > 50000
# "Interest Rate: 6%" for all others

age, income= int(input()), int(input())

if age > 60:
    print("Interest Rate: 8%")

elif income > 50000:
    print("Interest Rate: 7%")

else:
    print("Interest Rate: 6%")
