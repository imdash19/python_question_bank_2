# The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.

num = int(input())

while num != 1:
    print(num, end=" -> ")

    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

print(1)
