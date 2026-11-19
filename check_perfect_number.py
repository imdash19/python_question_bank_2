# Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

num = int(input())

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if num > 0 and total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
