# Write a function that identifies all duplicate elements in a list. The solution must run in linear time, meaning you should only traverse the list once.

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


numbers = list(map(int, input().split()))

print("Duplicate Elements:", find_duplicates(numbers))
