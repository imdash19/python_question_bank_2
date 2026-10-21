# A temperature log stores [30,32,31]. 
# The last reading was incorrect. 
# Take a new reading and replace the last value. 
# Print updated list.

lst= [30, 32, 21]
lst[-1]= int(input())
print(lst)
