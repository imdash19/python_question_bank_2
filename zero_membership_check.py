# Write a Python program to take a list of numbers as input.
# Check whether the value 0 is present in the list.
# Use membership checking to verify the condition.
# If zero exists in the list, print “Has Zero” otherwise print "Has no Zero".

lst= [int(val) for val in input().split()]
print('Has Zero' if 0 in lst else 'Has no Zero')
