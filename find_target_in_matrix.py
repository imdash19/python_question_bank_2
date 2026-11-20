# Given a 2D list (matrix), find the row and column index of a target value.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input())
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print("Row Index:", i)
            print("Column Index:", j)
            found = True
            break
    if found:
        break

if not found:
    print("Element not found")
