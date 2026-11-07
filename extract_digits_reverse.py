# Write a program to extract each digit from an integer in the reverse order.

num = int(input())

while num > 0:
    digit = num % 10
    print(digit)
    num //= 10
