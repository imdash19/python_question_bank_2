# Write a Python program to accept a string from the user.
# Check each character to see if it is a vowel (a, e, i, o, u).
# Consider both uppercase and lowercase vowels.
# Maintain a counter to count the number of vowels.
# Print the total vowel count clearly.

s= input()
cnt= 0
for v in s:
    if v in 'aeiou':
        cnt+= 1
print(cnt)
