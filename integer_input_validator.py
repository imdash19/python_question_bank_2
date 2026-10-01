# Reads a single integer from standard input within a constrained range (1 ≤ n ≤ 1000). The program validates the input and handles basic integer parsing.

try:
    n = int(input())

    if 1 <= n <= 1000:
        print("Valid input")
    else:
        print("Invalid input")

except ValueError:
    print("Invalid input")
