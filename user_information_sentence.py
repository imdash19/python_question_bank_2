# Write a Python program that asks for three pieces of information from the user: their name, age, and city. Store each piece of information in its own variable. Then, combine all three pieces of information into a nice, readable sentence and display it on the screen.
# For example, if someone enters their name as "John", age as "25", and city as "New York", your program should create a sentence like: "John is 25 years old and lives in New York."
# Input Format:

# First line: Name (text)
# Second line: Age (number)
# Third line: City (text)

# Output Format:
# A single sentence that combines all the information in a natural, easy-to-read way.

name= input()
age= int(input())
city= input()
print(f'{name} is {age} years old and lives in {city}.')
