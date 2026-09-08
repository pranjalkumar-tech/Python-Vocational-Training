# Sets
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Duplicate values are automatically removed
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# Adding an item
numbers.add(5)
print(numbers)

# Removing an item
numbers.remove(3)
print(numbers)

# Checking membership
print(2 in numbers)
print(10 in numbers)
#__________________________________________________________________________________________________________________________________________________________________________

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)

# Intersection
print(set1 & set2)

# Difference
print(set1 - set2)

# Symmetric Difference
print(set1 ^ set2)