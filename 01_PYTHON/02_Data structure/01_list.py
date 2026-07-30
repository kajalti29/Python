sales = [50, 30, 45, 60]
print(sales)

# Create list 
cities = ["Bhopal", "Indore", "Ujjain"]
print(cities)

# Indexing
cities = ["Indore", "Bhopal", "Ujjain"]
print(cities[0])
print(cities[1])

# Negative Indexing
cities = ["Indore", "Bhopal", "Ujjain"]
print(cities[-1])

# Slicing
sales = [10000, 20000, 30000, 40000, 50000]
print(sales[1:4])

# append()
cities = ["Indore", "Bhopal"]
cities.append("ujjain")
print(cities)

# pop()
cities = ["Indore", "Bhopal", "Ujjain"]
cities.pop(1)
print(cities)

# remove()
cities = ["Indore", "Bhopal", "Ujjain"]
cities.remove("Bhopal")
print(cities)

# Insert 
cities = ["Indore", "Ujjain"]
cities.insert(1, "Bhopal")
print(cities)

# sort()'
sales = [50000, 20000, 40000, 10000]
sales.sort()
print(sales)