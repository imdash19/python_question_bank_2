# Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

text = input()

found = False

for char in text:
    if char.isdigit():
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
