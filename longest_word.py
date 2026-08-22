# Write a Python program to accept a sentence as input.
# Split the sentence into individual words.
# Compare the length of each word in the sentence.
# Identify the word with the maximum length.
# Print the longest word clearly.

lst= list(input().split())

max_len= ''

for val in lst:
    if len(val) > len(max_len):
        max_len= val

print(max_len)
