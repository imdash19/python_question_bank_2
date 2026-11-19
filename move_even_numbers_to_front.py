# Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.

numbers = list(map(int, input().split()))

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

result = even_numbers + odd_numbers

print(result)
