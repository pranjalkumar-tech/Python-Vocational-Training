# Else
# else block runs when no exception occurs.

try:
    number = int(input("Enter a number: "))  # Takes integer input

except ValueError:
    print("Please enter a valid number.")

else:
    print("You entered:", number)  # Runs when there is no exception
#__________________________________________________________________________________________________________________________________________________________________________

# Finally
# finally block always runs whether an exception occurs or not.

try:
    number = int(input("Enter a number: "))  # Takes integer input
    print(number)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Program execution completed.")  # Always runs
#__________________________________________________________________________________________________________________________________________________________________________

# Raise
# raise is used to manually create an exception.

age = int(input("Enter your age: "))  # Takes age as input

if age < 0:
    raise ValueError("Age cannot be negative.")  # Raises an exception

print("Age:", age)