# Write a program to find how many times the substring “Emma” appears in a given string.

s= input().split()
cnt= 0
for v in s:
  if v == 'Emma':
    cnt+= 1

print(cnt)
