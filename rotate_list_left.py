# Given a list and an integer k, rotate the list to the left by k positions. For example, if k=2, the first two elements move to the end of the list.

numbers = list(map(int, input().split()))
k = int(input())

if numbers:
    k = k % len(numbers)
    rotated_list = numbers[k:] + numbers[:k]
    print(rotated_list)
else:
    print([])
