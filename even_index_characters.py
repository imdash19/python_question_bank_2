# Display only those characters which are present at an even index number in given string.

s= input()
for i in range(len(s)):
  if i%2 == 0:
    print(s[i])
