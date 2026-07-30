# A weather system stores each temperature as a separate record. 
# Take three readings and store them as ((t1,),(t2,),(t3,)). 
# Print the structure.

readings= ()
for i in range(3):
  temp= float(input())
  readings+= ((temp, ),)

print(readings)
