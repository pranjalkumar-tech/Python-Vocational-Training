# Common Built-in Exceptions

# ValueError
# Occurs when a value has an inappropriate type or format.
number = int("abc")  # Causes ValueError

# TypeError
# Occurs when an operation is performed on an inappropriate type.
result = "10" + 5  # Causes TypeError

# ZeroDivisionError
# Occurs when a number is divided by zero.
result = 10 / 0  # Causes ZeroDivisionError

# IndexError
# Occurs when an index is outside the range.
numbers = [1, 2, 3]
print(numbers[5])  # Causes IndexError

# KeyError
# Occurs when a key does not exist in a dictionary.
student = {"name": "Pranjal"}
print(student["age"])  # Causes KeyError