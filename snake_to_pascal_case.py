# Write a Python program to convert a snake_case string into PascalCase. 
# The program should take a string with words separated by underscores.
# Each word should start with a capital letter and no underscores should appear in output. 
# Output must preserve order.

text = input()

words = text.split("_")
pascal_case = "".join(word.capitalize() for word in words)

print(pascal_case)
