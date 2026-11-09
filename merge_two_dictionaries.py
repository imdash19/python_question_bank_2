# Write a program that takes two separate dictionaries and merges them into one single dictionary.

dict1 = {"name": "John", "age": 25}
dict2 = {"city": "Hyderabad", "country": "India"}

merged_dict = {**dict1, **dict2}

print(merged_dict)
