# Reads a single string from the user input with constraints on its length (1 ≤ len(s) ≤ 100). The program ensures the input is treated as a pure string without any type conversion.

text = input()

if 1 <= len(text) <= 100:
    print(text)
else:
    print("Invalid input")
