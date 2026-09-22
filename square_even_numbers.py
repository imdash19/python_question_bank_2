# Write a program to process only even numbers from a list. 
# The program should accept space-separated integers from the user.
# It should first filter even numbers from the list. 
# After filtering, it should compute the square of each even number. 
# Built-in filter() and map() functions must be used.
# The final output should contain only squared even numbers.

numbers = list(map(int, input().split()))

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared_numbers = list(map(lambda x: x ** 2, even_numbers))

print(squared_numbers)
