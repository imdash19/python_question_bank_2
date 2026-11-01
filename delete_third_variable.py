# Write a Python program to take three integer inputs in new lines.
# Print all three variables.
# Delete third variable using del keyword.
# Try accessing the deleted variable.
# Observe the runtime error.
# Note: After Observing the error correct the code. Dont print the deleted variables just print the non-deleted variables values as Shown in test cases

n1, n2, n3= int(input()), int(input()), int(input())
print(n1, n2, n3)
del n3
