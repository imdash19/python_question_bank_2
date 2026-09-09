# Write a program that takes space-separated integers as input in a single line. Use the map() function with a lambda function to calculate the square of each number in the list. The input will be integers separated by spaces, and the output should be the list of squared values in the same order.

square= lambda x: x**2
lst= list(map(int, input().split()))
slst= []

for val in lst:
    slst.append(square(val))

print(slst)
