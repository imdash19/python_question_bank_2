# Reads a text string and right-aligns it within a specified width using .format() method. Useful for numeric columns or right-justified text displays.

text = input()
width = int(input())

result = "{:>{}}".format(text, width)

print(result)
