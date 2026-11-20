# Given a nested list (a list containing other lists), write a program to “flatten” it into a single list containing all the individual elements.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat_list = []

for sublist in nested_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)
