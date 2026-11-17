# Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

rows = int(input())

for i in range(rows):
    letter = chr(65 + i)
    print((letter + " ") * (i + 1))
