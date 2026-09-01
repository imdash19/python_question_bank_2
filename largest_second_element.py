# Write a Python program to find the tuple with the largest second element from a list of user-entered tuples.
# The first line of input contains an integer N, the number of tuple rows.
# The next N lines each contain two space-separated values, forming a tuple.
# The first value can be a string or number, and the second value is always numeric.
# Print the entire tuple that has the maximum value in the second position [1st index].

n = int(input())

tuples_list = []

for _ in range(n):
    values = input().split()
    
    first = values[0]
    second = float(values[1])
    
    tuples_list.append((first, second))

largest_tuple = max(tuples_list, key=lambda x: x[1])

print(largest_tuple)
