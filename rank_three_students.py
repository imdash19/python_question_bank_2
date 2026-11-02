# Write a Python program to read marks of three students.
# Arrange the marks from highest to lowest.
# Assign First, Second, and Third ranks.
# Print the ranks clearly.

marks= list(map(int, input().split()))
marks= sorted(marks, reverse= True)
print(f'First: {marks[0]}Second: {marks[1]}Third: {marks[2]}')
