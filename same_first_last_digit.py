# Write a Python program to take a number as input.
# Extract the first digit and the last digit of the number.
# Compare both digits using a condition.
# If they are the same, print “Same First and Last Digit”.

n= abs(int(input()))
fdigit= int(str(n)[0])
ldigit= int(str(n)[-1])

print('Same First and Last Digit' if fdigit == ldigit else '')
