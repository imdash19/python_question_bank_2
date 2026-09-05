# Write a function that accepts any number of integers using variable
# length arguments. The function should calculate and return the
# sum of all values. The inputs are entered one per line in the console.
# The program should handle three integer inputs and returns the sum value by using *args.

def calculate_sum(*args):
    return sum(args)


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = calculate_sum(num1, num2, num3)

print(result)
