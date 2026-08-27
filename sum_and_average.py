# Write a Python program to calculate the sum of all elements in a list.
# Use the sum() function for total.
# Divide the sum by the number of elements to get the average.
# Print both sum and average clearly.

lst= list(map(int, input().split()))
print(f'''Sum: {sum(lst)}
Average: {sum(lst)/len(lst)}''')
