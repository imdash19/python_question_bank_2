# Write a Python program to find the largest and smallest elements in a list.
# Use the max() and min() functions to get values.
# Print the maximum and minimum clearly.

lst= list(map(int, input().split()))
max_num= max(lst)
min_num= min(lst)
print(f'''Max: {max_num} 
Min: {min_num}''')
