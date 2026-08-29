# Write a Python program to accept a list of integer elements.
# Initialize a counter variable to 0.
# Use a loop to iterate through each element and increment the counter by 1.
# After the loop ends, the counter will hold the length of the list.
# Print the total count clearly as the length.

numbers = list(map(int, input().split()))

count = 0

for number in numbers:
    count += 1

print("Length:", count)
