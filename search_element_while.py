# Write a Python program to search for a specific number in a list.
# Accept a list of numbers and a search element from the user.
# Use a while loop to traverse the list using an index.
# If the element is found, print “Found” and break the loop.
# Use the else block to print “Not Found” if the search fails.

lst= list(map(int, input().split()))
n= int(input())

print('Found' if n in lst else 'Not Found')
