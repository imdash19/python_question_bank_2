# Given a list, iterate it in reverse order and print each element.

numbers = list(map(int, input().split()))

for num in reversed(numbers):
    print(num)
