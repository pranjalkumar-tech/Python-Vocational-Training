# Try and Except

# try block contains code that may cause an exception.
try:
    number = int(input("Enter a number: "))  # Takes integer input
    print(number)

# except block handles the exception.
except ValueError:
    print("Please enter a valid number.")