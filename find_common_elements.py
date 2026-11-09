# Take two lists and find the elements that appear in both. Use Sets to perform the operation.

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

common_elements = set(list1) & set(list2)

print(common_elements)
