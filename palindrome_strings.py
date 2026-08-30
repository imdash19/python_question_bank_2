# Write a Python program to accept a list of strings.
# Use list comprehension to check each string for palindrome condition.
# Compare each string with its reverse.
# Store only palindrome strings in a list.
# Print the final list.

strings = input().split()

palindromes = [word for word in strings if word == word[::-1]]

print(palindromes)
