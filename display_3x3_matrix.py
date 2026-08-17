# Write a Python program to display all elements of a 3×3 matrix.
# Use a predefined 2D list containing three rows and three columns.
# Apply an outer loop to iterate through each row of the matrix.
# Use an inner loop to access each element in the current row.
# Print elements in matrix form, maintaining row and column structure.
# This Is Your matrix = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for val in matrix:
  for v in val:
    print(v, end= ' ')
  print()
