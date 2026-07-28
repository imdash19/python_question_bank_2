# A class register stores multiple student records. 
# Take three student name-mark pairs and store them as a nested tuple. 
# Print the structure.

register= []
for i in range(3):
  tup= (input(), int(input()))
  register.append(tup)
  
register= tuple(register)
print(register)
