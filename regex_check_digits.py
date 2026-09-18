# You need to write a program that checks if a string contains any numbers (digits 0-9) in it. The program should ask the user to enter any text or sentence. Then, it should check whether there are any digits present in that text and tell the user if digits are found or not. You will use Python's re module (regular expression) to search for digits without using any loops or manual checking.
# Input Format:

# A single line containing a string (text, sentence, or any combination of characters)

# Output Format:

# Print "Digits present" if the string contains any digit
# Print "Digits not present" if the string does not contain any digit

import re

text = input()

if re.search(r"\d", text):
    print("Digits present")
else:
    print("Digits not present")
