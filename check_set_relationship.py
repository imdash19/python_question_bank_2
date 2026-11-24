# Write a script that takes two lists of integers from a user, converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

set1 = set(list1)
set2 = set(list2)

if set1.issubset(set2):
    print("Subset")
elif set1.issuperset(set2):
    print("Superset")
elif set1.isdisjoint(set2):
    print("Disjoint")
else:
    print("Neither Subset, Superset nor Disjoint")
