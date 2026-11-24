# Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] = [merged_dict[key], value]
    else:
        merged_dict[key] = value

print(merged_dict)
