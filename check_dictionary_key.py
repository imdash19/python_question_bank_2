# Write a Python program to check if a key exists in a dictionary.
# The user enters the dictionary key-value pairs one by one, specifying the number of items.
# Then the user enters the key they want to check.
# The program prints True if the key exists, False otherwise.

n = int(input())

my_dict = {}

for _ in range(n):
    key, value = input().split()
    my_dict[key] = value

search_key = input()

print(search_key in my_dict)
