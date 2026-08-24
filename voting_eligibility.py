# Write a Python program to read the age of a person.
# Check voting eligibility in India (18) and USA (21).
# Print Eligible in both if eligible in both countries.
# Otherwise, print Not eligible in both.

age= int(input())

print('Eligible in both' if age > 18 and age > 25 else 'Not eligible in both')
