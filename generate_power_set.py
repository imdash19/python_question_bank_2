# Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).

def power_set(original_set):
    result = [set()]

    for element in original_set:
        new_subsets = []

        for subset in result:
            new_subset = subset.copy()
            new_subset.add(element)
            new_subsets.append(new_subset)

        result.extend(new_subsets)

    return result


numbers = set(map(int, input().split()))

print(power_set(numbers))
