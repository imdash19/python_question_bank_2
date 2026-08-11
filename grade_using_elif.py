# Write a Python program to take a student’s marks as input.
# Use ELIF conditions to compare the marks with given ranges.
# Assign grade A if marks are greater than 90.
# Assign B if marks are between 70 and 90, C if between 50 and 70.
# Print Fail if marks are less than 50.

marks = int(input())

if marks > 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
