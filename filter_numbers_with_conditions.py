# Given a list of numbers, iterate through it and print numbers that satisfy these conditions:

# The number must be divisible by five.
# If the number is greater than 150, skip it and move to the next.
# If the number is greater than 500, stop the loop entirely.

lst= list(map(int, input().split()))

for val in lst:
  if val % 5 == 0:
    if val > 150:
      pass
    elif val > 500:
      break
