# A class register stores multiple student records. 
# Take three student name-mark pairs and store them as a nested list. 
# Print the structure.

records= [int(val) if val.lstrip('-').isdigit() else val for val in input().split()]

records= [records[i:i+2] for i in range(0, len(records)-1, 2)]

print(records)
