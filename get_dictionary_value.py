# Write a Python program to retrieve a value from a dictionary using a key.
# The user enters the dictionary key-value pairs one by one, specifying how many items to enter.
# Then the user enters the key they want to access.
# The program prints the corresponding value clearly.

n = int(input())

my_dict = {}

for _ in range(n):
    key, value = input().split()
    my_dict[key] = value

search_key = input()

print(my_dict[search_key])
