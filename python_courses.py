fruits = ("cherry", "melone", "pineapple","banana", "peach","apple", "pineapple")

print(fruits[2])
print(len(fruits))


city = ("Vienna",)
print(city)
print(type(fruits))

cities = tuple(("Warsaw", "Vienna", "Tehran", "London"))
print(cities[0:3])

if "Berlin" in cities:
  print("The value is in tuple")


# add new value to tuple 
  # method 1
# new_cities = list(cities)
# print(new_cities)
# new_cities.append("Stockholm")
# print(new_cities)

# updated_cities = tuple(new_cities)
# print(updated_cities)

  # method 2 
# new_cities = ("Madrid", "Lisbon")
# modified_cities = cities + new_cities
# print(modified_cities)

# remove item from tuple
# new_cities = list(cities)
# new_cities.pop(2)
# print(new_cities)
# modified_cities = tuple(new_cities)
# print(modified_cities)

(capita_city1, capita_city2, *remained_cities) = cities 
print(capita_city1, capita_city2, remained_cities)