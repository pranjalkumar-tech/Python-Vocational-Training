# Tuples
tuple = ("Apple", 1, 1.55, True, None, 12345)
print(tuple)
#__________________________________________________________________________________________________________________________________________________________________________

# Indexing
fruits = ("Apple", "Mango", "Banana")

print(fruits[0])  # Print Apple at 0
print(fruits[1])  # Print Mango at 1
print(fruits[2])  # Print Banana at 2

print(fruits[-3])  # Print Apple at -3
print(fruits[-2])  # Print Mango at -2
print(fruits[-1])  # Print Banana at -1

# Slicing
fruits = ("Apple", "Mango", "Banana", "Grapes")

print(fruits[1:3])  # Print Mango and Grapes at index 1 and 3
print(fruits[0:2])  # Print Apple and Mango at index 0 and 2
#__________________________________________________________________________________________________________________________________________________________________________

# Tuple Methods

# Length of a Tuple
fruits = ("Apple", "Mango", "Banana")
print(len(fruits))

# Count an Element
numbers = (1, 2, 3, 4, 5, 1, 2, 1)
print(numbers.count(1))  # Count the number of times 1 appears in the tuple

# Find Index of an Element
numbers = (1,2,3,4,5)
print(numbers.index(4))  # show at which index 4 is present

# Loops
numbers = (1,2,3,4,5)
for x in numbers:
    print(x)

# Membership Operators
fruits = ("Apple", "Mango", "Banana")
print("Mango" in fruits)  # True
print("Grapes" in fruits)  # False

# Join two tuples using
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Repition of a tuple
tuple1 = (1,2,3)
print(tuple1 * 3)  # Repeat tuple 3 times

# Tuple Packing
student = ("Pranjal", 20, "CSE")  # Pack values into a tuple
print(student)

# Tuple Unpacking
student = ("Pranjal", 20, "CSE")
name, age, course = student  # Unpack the tuple
print(name)
print(age)
print(course)

# Create a nested tuple
marks = (
    (90, 85),
    (78, 88)
)
print(marks[0][0])  # prints 90

# Converting a tuple into list
fruits = ("Apple", "Mango", "Banana")
fruit_list = list(fruits)
print(fruit_list)