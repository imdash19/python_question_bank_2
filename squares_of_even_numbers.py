# Given a list of numbers, use map() and filter() together to create a list of the squares of only the even numbers.

numbers = list(map(int, input().split()))

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(result)
