# Write a program that takes a year as input and determines if it is a leap year.

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
