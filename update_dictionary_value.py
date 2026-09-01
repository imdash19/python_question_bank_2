# Write a Python program to update the value of a key in a dictionary.
# The user enters the dictionary key-value pairs one by one, specifying the number of items.
# Then the user enters the key they want to update and the new value.
# The program prints the updated dictionary.

n = int(input())

my_dict = {}

for _ in range(n):
    key, value = input().split()
    my_dict[key] = value

key_to_update = input()
new_value = input()

my_dict[key_to_update] = new_value

print(my_dict)
