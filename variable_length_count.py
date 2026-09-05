# Write a function that accepts variable length arguments and counts 
# how many values were passed. The program should print the total 
# count. Inputs are provided one per line. This helps understand 
# how *args stores values internally. The function should work for
# any number of inputs.

def count_values(*args):
    return len(args)


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = count_values(num1, num2, num3)

print(result)
