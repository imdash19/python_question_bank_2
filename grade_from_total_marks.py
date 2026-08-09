# Write a Python program to take marks of 5 subjects separately.
# Calculate the total marks obtained.
# Assign grade A if total is greater than 90, B if greater than 80.
# Assign C if greater than 70, D if greater than 60, else F.

s1, s2, s3, s4, s5= int(input()), int(input()), int(input()), int(input()), int(input())
total= s1+s2+s3+s4+s5
print('A' if total >= 90 else 'B' if total >= 80 else 'C' if total >= 70 else 'D' if total >= 60 else 'F')
