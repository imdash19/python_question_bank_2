# Write a Python program to read student marks.
# Assign grades based on given ranges.
# • 90–100 → A
# • 75–89 → B
# • 60–74 → C
# • Below 60 → Fail

mark= int(input())
print('A' if 100 >= mark >= 90 else 'B' if 89 >= mark >= 75 else 'C' if 74 >= mark >= 60 else 'Fail')
