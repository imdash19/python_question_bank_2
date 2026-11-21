# Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.

def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


nested_list = [1, [2, 3], [4, [5, 6]], 7]

print(flatten_list(nested_list))
