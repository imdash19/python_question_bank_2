# Beginner-Friendly Python Question

# 1. Problem Statement Description
# You need to create a program that formats text with right-alignment. Right-alignment means the text is pushed to the right side, with spaces added on the left to fill up the total width.
# Here's how it works:

# You have a text string that you want to display
# You have a specific width (total number of characters) for displaying the text
# The text should appear on the right side of this width
# Empty spaces will be added on the left side to fill the remaining width

# Example: If your text is "Hello" and width is 10, the output will be "     Hello" (5 spaces on the left, then "Hello")
# You need to create a program that:

# Takes a text string as input
# Takes the total width (number of characters) as input
# Displays the text right-aligned within that width using modern f-string formatting

# Input Format:

# First line: Text string (string)
# Second line: Total width for alignment (integer)

# Output Format:

# Print the right-aligned text within the specified width

text = input()
width = int(input())

print(f"{text:>{width}}")
