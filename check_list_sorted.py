# Write a Python program to check whether a list is sorted in ascending order.
# Accept a list of numbers from the user.
# Use a for loop to compare each element with the next one.
# If any element is greater than the next, break the loop.
# Use the else block to confirm the list is sorted.
# Print the appropriate result.

lst= list(map(int, input().split()))

sorted_lst= sorted(lst)

print('Sorted' if lst == sorted_lst else 'Not Sorted')
