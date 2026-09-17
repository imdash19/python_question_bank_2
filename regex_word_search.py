# You need to write a program that checks if a specific word appears in a sentence or text. The program should ask the user to enter a sentence first, then ask for a word to search. After that, it should tell whether that exact word exists in the sentence or not. Remember, the search is case-sensitive, which means "Hello" and "hello" are treated as different words. You will use Python's re module (regular expression) to perform this search.Input Format:

# First line: A string (sentence or text)
# Second line: A word to search for
# Output Format:

# Print "Word found" if the word exists in the string
# Print "Word not found" if the word does not exist in the string

import re

sentence = input()
word = input()

if re.search(r"\b" + re.escape(word) + r"\b", sentence):
    print("Word found")
else:
    print("Word not found")
