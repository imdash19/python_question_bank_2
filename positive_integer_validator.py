# Reads an integer from input and validates that it is a positive number (n > 0). The program provides appropriate feedback for valid and invalid inputs.

try:
    n = int(input())

    if n > 0:
        print("Valid input")
    else:
        print("Invalid input")

except ValueError:
    print("Invalid input")
