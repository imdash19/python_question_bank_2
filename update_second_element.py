# Write a Python program to accept a list of integer elements.
# Allow the user to provide a new value to replace the second element.
# Use indexing to access and update the second element (list[1]).
# Store the updated list.
# Print the final list clearly to show the change.
# Note: List indexing starts from 0 not from 1 and with -1 in the reverse order

numbers = list(map(int, input().split()))
new_value = int(input())

numbers[1] = new_value

print(numbers)
