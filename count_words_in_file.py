# Write a script that opens an existing .txt file and counts the total number of words it contains.

filename = input()

with open(filename, "r") as file:
    content = file.read()
    words = content.split()

print("Total Words:", len(words))
