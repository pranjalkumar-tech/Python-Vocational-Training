# 10. Create a function to check whether a number is prime.
# Function: isPrime(int n)

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if isPrime(n):
    print("Prime")
else:
    print("Not a prime")
# ____________________________________________________________________________________________________


# 11. Create a function to calculate the power of a number.
# Function: power(int base, int exponent)

def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Power:", power(base, exponent))
# ____________________________________________________________________________________________________


# 12. Create a function to check whether a year is a leap year.
# Function: isLeapYear(int year)

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter year: "))

if isLeapYear(year):
    print("Leap year")
else:
    print("Not a leap year")
# ____________________________________________________________________________________________________


# 13. Create a function to find the sum of digits of a number.
# Function: sumOfDigits(int n)

def sumOfDigits(n):
    n = abs(n)
    result = 0

    while n > 0:
        digit = n % 10
        result = result + digit
        n = n // 10

    return result

n = int(input("Enter a number: "))
print("Sum of digits:", sumOfDigits(n))
# ____________________________________________________________________________________________________


# 14. Create a function to calculate the area of a circle.
# Function: areaOfCircle(double radius)

def areaOfCircle(radius):
    return 3.14 * radius * radius  # Calculates area of circle

radius = float(input("Enter radius: "))
print("Area of circle:", areaOfCircle(radius))
# ____________________________________________________________________________________________________


# 15. Create a function to convert Celsius to Fahrenheit.
# Function: celsiusToFahrenheit(double celsius)

def celsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32  # Converts Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit:", celsiusToFahrenheit(celsius))
# ____________________________________________________________________________________________________


# 16. Create a menu-driven calculator using functions.
# Functions:
# add()
# subtract()
# multiply()
# divide()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

while True:
    print("\n----- Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator closed")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")