# Print a downward half-pyramid pattern using stars (*).

n= int(input())

for i in range(m, 0, -1):
  for j in range(i):
    print('*', end= ' ')
  print()
