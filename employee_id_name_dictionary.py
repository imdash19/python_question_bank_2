# Accept employee id list and name list create dictionary using zip

emp_ids = input().split()
names = input().split()

employee_dict = dict(zip(emp_ids, names))

print(employee_dict)
