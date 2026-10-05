# Reads name and score values, then outputs a formatted string using named placeholders with .format() method. Demonstrates clearer formatting with descriptive placeholder names.

name, score= input(), int(input())
print('Student:{},Score:{}'.format(name, score))
