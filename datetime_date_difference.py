# Write a Python program to calculate number of days between two dates.
# Input two dates in YYYY-MM-DD format.
# Use datetime.date objects.
# Subtract dates to get timedelta.
# Dot notation must be used.
# Print the difference in days.

from datetime import date

date1 = input()
date2 = input()

d1 = date.fromisoformat(date1)
d2 = date.fromisoformat(date2)

difference = d2 - d1

print(difference.days)
