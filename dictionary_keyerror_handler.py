# Write a Python program to handle missing keys in a dictionary using exception handling.
# Here's what you need to do:

# Create a dictionary named scores with the following student names and their scores: Alice with score 85, Bob with score 92, Charlie with score 78, and David with score 90.
# Take a student name as input from the user.
# Use a try block to access the score for that student name from the dictionary.
# If the name exists in the dictionary, display the score in the format "Score: [score]".
# Use an except block to catch the KeyError exception if the name is not found in the dictionary.
# Display an appropriate error message when the key is missing.
# The program should not crash even if the key doesn't exist.

# Input Format:

# Single line contains a student name as a string.

# Output Format:

# If name exists: Display "Score: [score]".
# If name doesn't exist: Display "Error: Name not found in the dictionary".

scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

name = input()

try:
    score = scores[name]
    print("Score:", score)

except KeyError:
    print("Error: Name not found in the dictionary")
