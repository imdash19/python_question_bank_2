# Reads name and score values, then outputs a formatted string using f-string with direct variable access. Shows the most concise named formatting approach.

name, score= input().split()
print(f'"Student: {name}, Score: {score}"')
