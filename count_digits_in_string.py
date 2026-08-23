# Write a Python program to accept a string from the user.
# Check each character to determine whether it is a digit (0–9).
# Use a counter to track how many digits are found.
# Ignore non-digit characters safely.
# Print the total number of digits present.

s= input()
cnt= 0

for v in s:
    if v.isdigit():
        cnt+= 1

print(cnt)
