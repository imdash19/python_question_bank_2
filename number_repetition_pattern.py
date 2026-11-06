# Print the following pattern where each row contains a number repeated a specific number of times based on its value.

n= int(input())
for i in range(1, n+1):
  for j in range(1, i+1):
    print(i)
  print()
