# Lists
words = ["Apple", "Banana", 12345, "Oranges", None]
print(words)
#__________________________________________________________________________________________________________________________________________________________________________

# Indexing
fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])  # Print Apple at 0
print(fruits[1])  # Print Mango at 1
print(fruits[2])  # Print Banana at 2

print(fruits[-3])  # Print Apple at -3
print(fruits[-2])  # Print Mango at -2
print(fruits[-1])  # Print Banana at -1

# Slicing
fruits = ["Apple", "Mango", "Banana", "Grapes"]

print(fruits[1:3])  # Print Mango and Grapes at index 1 and 3
print(fruits[0:2])  # Print Apple and Mango at index 0 and 2
#__________________________________________________________________________________________________________________________________________________________________________

# List Methods

# Changing List Elements
fruits = ["Apple", "Mango", "Banana"]
fruits[1] = "Orange"  # Change Mango to Orange
print(fruits)

# Adding Elements
fruits = ["Apple", "Mango", "Banana"]
fruits.append("Coconut")  # Adds Coconut to the end of fruit list
print(fruits)

# insert()
fruits = ["Apple", "Mango", "Banana"]
fruits.insert(2, "Grapes")  # Adds Grapes at 2
print(fruits)

# extend()
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)  # Adds list2 to list 1
print(list1)

# Removing Elements
fruits = ["Apple", "Mango", "Banana"]
fruits.remove("Mango")  # Removes an element by value
print(fruits)

# pop()
fruits = ["Apple", "Mango", "Banana"]
fruits.pop(1)  # Removes an element by index
print(fruits)

# del()
fruits = ["Apple", "Mango", "Banana"]
del fruits[0]  # removes an element
print(fruits)
# Another example
fruits = ["Apple", "Mango", "Banana"]
del fruits[0:3]  # removes the whole list
print(fruits)

# clear()
fruits = ["Apple", "Mango", "Banana"]
fruits.clear()  # removes all the elements from the list
print(fruits)

# Sorting
list = [100, 33, 66, 77, 44]
list.sort()  # Sorts the list in ascending order
print(list)

# Reverse
list = [100, 33, 66, 77, 44]
list.reverse()  # Sorts the list in reverse order(It does not sort the list)
print(list)

# Copy a List
list1 = [1, 2, 3, 4]
list2 = list1.copy()  # list1 is copied to list2
print(list2)

# Length of a List
list = [1, 2, 3, 4]
print(len(list))  # prints length of list

# Loop
list = [1, 2, 3, 4]
for x in list:
    print(x)

# Membership Operators
fruits = ["Apple", "Mango", "Banana"]
print("Mango" in fruits)  # True
print("Grapes" in fruits)  # False

# Create a nested list
marks = [
    [90, 85],
    [78, 88]
]
print(marks[0][0])  # prints 90
print(marks[0][1])  # prints 85
print(marks[1][0])  # prints 78
print(marks[1][1])  # prints 88