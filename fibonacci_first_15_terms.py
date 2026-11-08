# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

a = 0
b = 1

for i in range(15):
    print(a, end=" ")
    a, b = b, a + b
