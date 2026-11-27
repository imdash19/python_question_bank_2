# Create a generator function that yields Fibonacci numbers up to N. Instead of returning a full list, it should yield values one by one.

def fibonacci_generator(n):
    a, b = 0, 1

    while a <= n:
        yield a
        a, b = b, a + b

n = int(input("Enter the limit: "))

for num in fibonacci_generator(n):
    print(num, end=" ")
