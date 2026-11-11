# Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

squares = {}

for num in range(1, 11):
    squares[num] = num ** 2

print(squares)
