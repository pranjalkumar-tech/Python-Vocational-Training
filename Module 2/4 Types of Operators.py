# Types of Operators

# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)  # Add
print("Subtraction:", a - b)  # Subtract
print("Multiplication:", a * b)  # Multiply
print("Division:", a / b)  # Divide
print("Modulus:", a % b)  # Helps to find the remainder
print("Exponentiation:", a**b)  # Multiply a by itself b times
print("Floor Division:", a // b)  # Divide a by b and round down to the nearest whole number
# __________________________________________________________________________________________________________________________________________________________________________


# Assignment Operators
x = 10
print(x)  # Assign the value 10 to x

x = 10
x += 5
print(x)  # Add and Assign

x = 10
x -= 3
print(x)  # Subtract and Assign

x = 10
x *= 2
print(x)  # Multiply and Assign

x = 10
x /= 2
print(x)  # Divide and Assign

x = 10
x %= 3
print(x)  # Modulus and Assign

x = 5
x **= 2
print(x)  # Exponentiation and Assign

x = 10
x //= 3
print(x)  # Floor Division and Assign
# __________________________________________________________________________________________________________________________________________________________________________


# Comparison Operators
a = 10
b = 5
print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal
print(a <= b)  # Less than or equal
# __________________________________________________________________________________________________________________________________________________________________________


# Logical Operators: Check multiple conditions.
# Truth table of 'or' operator
# If anyone is true then the result is true
print("True or False is ", True or False)  # it will return true
print("True or True is ", True or True)  # it will return true
print("False or True is ", False or True)  # it will return true
print("False or False is ", False or False)  # it will return false

# Truth table of 'and' operator
# If anyone is false then the result is false
print("True and False is ", True and False)  # it will return false
print("True and True is ", True and True)  # it will return true
print("False and True is ", False and True)  # it will return false
print("False and False is ", False and False)  # it will return false

# truth table of 'not' operator
# It reverse the value of the operand
print(not (True))  # it will return false
print(not (False))  # it will return true
# __________________________________________________________________________________________________________________________________________________________________________


# Identity Operators: # Check if both variables refer to the same object
# is Operator
x = 10  # Assign 10 to x
y = x  # # y refers to the same object as x
print(x is y)  # It is true, because both variables refer to the same object

# is not operator
x = [10, 20]  # Create first list
y = [10, 20]  # Create second list with same values
print(x == y)  # Compare values
print(x is y)  # Compare objects
# __________________________________________________________________________________________________________________________________________________________________________


# Membership Operators
# in operator
# # 1st example: on string
name = "Pranjal"  # Create a string
print("P" in name)  # Check if 'P' is present in the string
# 2nd example: on list
numbers = [10, 20, 30, 40]  # Create a list
print(20 in numbers)  # Check if 20 is present in the list

# not in operator
# 1st example: on string
name = "Pranjal"  # Create a string
print("k" not in name)  # Check if 'k' is not present in the string
# 2nd example: on list
numbers = [10, 20, 30, 40]  # Create a list
print(50 not in numbers)  # Check if 50 is not present in the list
