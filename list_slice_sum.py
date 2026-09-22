# Write a Python program to calculate the sum of elements in a list between two given indices.
# The program should accept a space-separated list of numbers from the user.
# It should accept two integers representing the start index and end index.
# Use list slicing to extract elements between the indices.
# Use Python’s built-in sum() function to calculate the total.
# Display the sum clearly.

numbers = list(map(int, input().split()))

start = int(input())
end = int(input())

result = sum(numbers[start:end])

print(result)
