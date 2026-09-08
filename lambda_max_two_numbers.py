# Write an anonymous function to find the maximum of two numbers. Inputs are space-separated integers.
# The program should output the larger value. This helps understand conditional logic inside 
# anonymous functions. Handle equal values correctly.

max_num= lambda x, y: x if x > y else y
print(max_num(int(input()), int(input())))
