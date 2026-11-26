# Implement the Binary Search algorithm recursively to find a target value in a sorted list.

def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid
    elif target < numbers[mid]:
        return binary_search(numbers, target, left, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, right)


numbers = list(map(int, input().split()))
target = int(input())

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
