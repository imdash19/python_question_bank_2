# Reads name and age values, then outputs a formatted string using Python's %-formatting operator. Demonstrates legacy string formatting approach.

name = input()
age = int(input())

message = "My name is %s and I am %d years old." % (name, age)

print(message)
