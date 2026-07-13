# A list contains [10,20,30]. 
# Take a number and insert it at the last position using insert(). 
# Print the list.

numbers = [10, 20, 30]

num = int(input())

numbers.insert(len(numbers), num)

print(numbers)
