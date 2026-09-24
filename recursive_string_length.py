# Write a program to find the length of a string using recursion.
# The program should count one character at a time.
# It should recursively call itself with the remaining substring.
# The base case is when the string becomes empty. 
# The output is total character count.

def string_length(text):
    if text == "":
        return 0

    return 1 + string_length(text[1:])


text = input()

print(string_length(text))
