# A store wants to increase each product price by 10 units. 
# Take two prices as input and create a new list with the increased values using list comprehension.

lst= list(map(int, input().split()))
nlst= [(val + 10) for val in lst]
print(nlst)
