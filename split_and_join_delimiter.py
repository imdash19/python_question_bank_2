# Write a Python program to split a string into words and then join them with a delimiter. 
# The program should accept string input and delimiter. Words are separated by spaces. 
# Output should display the joined string.

text = input()
delimiter = input()

words = text.split()
result = delimiter.join(words)

print(result)
