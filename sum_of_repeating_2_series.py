# Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.

n = int(input())

term = 0
total = 0

for i in range(n):
    term = term * 10 + 2
    total += term

print("Sum:", total)
