# Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

for i in range(2, 21):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    print(i, end= ' ')
