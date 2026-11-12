# Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

with open("notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("Django is a Python framework.\n")
    file.write("I love programming.\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
