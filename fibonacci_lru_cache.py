# Write a recursive function fibonacci(n) to calculate the nth number in the Fibonacci sequence. Use functools.lru_cache to optimize it so that it doesn’t recalculate the same values multiple times.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"Fibonacci number at position {n}: {fibonacci(n)}")
