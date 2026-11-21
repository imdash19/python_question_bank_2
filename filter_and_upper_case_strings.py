# Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.

words = input().split()

result = [word.upper() for word in words if len(word) >= 4]

print(result)
