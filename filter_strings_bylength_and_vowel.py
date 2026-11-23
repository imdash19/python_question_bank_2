# Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

words = input().split()

result = [word for word in words if len(word) > 5 and word[0].lower() in "aeiou"]

print(result)
