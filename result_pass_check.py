# Create class Result with instance method check_pass that prints Pass if marks >=40 else Fail

class Result:
    def check_pass(self, mark):
        return 'Pass' if mark >= 40 else 'Fail'

print(Result().check_pass(int(input())))
