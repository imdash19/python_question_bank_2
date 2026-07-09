# A theater assigns four even-numbered seats. 
# Take four even numbers as input, store them in a list, and print the list.

lst= [int(val) for val in input().split() if int(val)%2 == 0]
print(lst)
