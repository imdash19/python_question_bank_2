# The program should read integer values only.
# The user enters elements of two sets in separate lines.
# The intersection contains only the elements that are common in both sets.
# Duplicate values must not appear in the result.
# Since sets are unordered, convert the result into a sorted list before displaying.
# Display the final result clearly.

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

intersection = set1.intersection(set2)

result = sorted(intersection)

print(result)
