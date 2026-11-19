# Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
