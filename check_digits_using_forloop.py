# Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

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
