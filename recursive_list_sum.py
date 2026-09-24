# Write a program to calculate the sum of all elements in a list using recursion. 
# The program should add the first element and recursively call for remaining elements. 
# The recursion stops when the list is empty. Output is total sum.

def list_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + list_sum(numbers[1:])


numbers = list(map(int, input().split()))

print(list_sum(numbers))
