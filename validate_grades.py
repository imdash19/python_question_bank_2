# Write a Python program to read three grades.
# Check if all grades are between 0 and 10.
# Print Valid Grades if all are in range.
# Otherwise, print Invalid Grades.

g1, g2, g3= int(input()), int(input()), int(input())

print('Valid Grades' if 0 <= g1 <= 10 and 0 <= g2 <= 10 and 0 <= g3 <= 10 else 'Invalid Grades')
