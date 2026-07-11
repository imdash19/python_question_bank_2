# Accept city list and pincode list create dictionary using zip

cities = input().split()
pincodes = list(map(int, input().split()))

city_pincode = dict(zip(cities, pincodes))

print(city_pincode)
