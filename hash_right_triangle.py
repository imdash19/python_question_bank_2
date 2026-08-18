# Write a Python program to print a right-angled triangle using #.
# Use nested loops to control rows and columns.
# The outer loop decides the current row number.
# The inner loop prints hashes equal to the row count.
# Each row should appear on a new line.

n= int(input())
for i in range(1, n+1):
    for j in range(i):
        print('#', end= ' ')
    print()
