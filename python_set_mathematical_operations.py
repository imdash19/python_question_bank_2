# Sets are not just for removing duplicates; they are powerful mathematical tools for comparing collections. Using set logic is much faster and more readable than writing multiple for loops with if conditions.

set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
print("Is Subset:", set1 <= set2)
print("Is Superset:", set1 >= set2)
