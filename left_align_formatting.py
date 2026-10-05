# Reads a text string and left-aligns it within a specified width using .format() method. Useful for creating consistently formatted text columns.

text = input()
width = int(input())

result = "{:<{}}".format(text, width)

print(result)
