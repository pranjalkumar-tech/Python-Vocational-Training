# Multiple Exceptions

try:
    number = int(input("Enter a number: "))  # Takes integer input
    result = 10 / number  # Divides 10 by the number
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")