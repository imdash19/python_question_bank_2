# Create a class PowerOfTwo that allows you to iterate through powers of 2 (1, 2, 4, 8…) up to a specified maximum exponent.

class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.exponent > self.max_exponent:
            raise StopIteration

        result = 2 ** self.exponent
        self.exponent += 1

        return result


max_exponent = int(input())

for number in PowerOfTwo(max_exponent):
    print(number)
