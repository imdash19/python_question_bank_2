# Accept city list and pincode list create dictionary using zip

c1, c2= input().split()
p1, p2= map(int, input().split())
d= {}

d[c1]= p1
d[c2]= p2

print(d)
