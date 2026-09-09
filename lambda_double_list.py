# Write a program that takes space-separated integers as input in a single line. Use the map() function with a lambda function to double each number in the list (multiply by 2). The input will be integers separated by spaces, and the output should be the list of doubled values in the same order.

double= lambda x: x*2
lst= list(map(int, input().split()))
dlst= []

for val in lst:
    dlst.append(double(val))

print(dlst)
