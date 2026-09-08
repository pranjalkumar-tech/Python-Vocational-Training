# Custom Exception
# We can create our own exception using a class.

class AgeError(Exception):  # Creates a custom exception
    pass

age = int(input("Enter your age: "))  # Takes age as input

if age < 18:
    raise AgeError("You must be 18 or above.")  # Raises custom exception

print("You are eligible.")