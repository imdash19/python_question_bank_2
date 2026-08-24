# Write a Python program to read marks of three subjects.
# Check if marks in each subject are 40 or more.
# Print Pass if all subjects are passed.
# Otherwise, print Fail.

m1, m2, m3= int(input()), int(input()), int(input())

print('Pass' if m1 >= 40 and m2 >= 40 and m3 >= 40 else 'Fail')
