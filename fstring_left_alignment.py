# Reads a text string and left-aligns it within a specified width using f-string syntax. Modern approach to text alignment formatting.

text = input()
width = int(input())

result = f"{text:<{width}}"

print(result)
