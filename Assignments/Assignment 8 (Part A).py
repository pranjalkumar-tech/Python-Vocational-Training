# 1. Create a function to find the square of a number.
# Function: square(int n)

def square(n):
    return n * n  # Returns the square of the number

n = int(input("Enter a number: "))
print("Square:", square(n))
# ____________________________________________________________________________________________________


# 2. Create a function to print your name.
# Function: printName()

def printName():
    print("My Name")

printName()
# ____________________________________________________________________________________________________


# 3. Create a function to add two numbers and print the result.
# Function: add(int a, int b)

def add(a, b):
    return a + b  # Returns the sum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", add(a, b))
# ____________________________________________________________________________________________________


# 4. Create a function to check whether a number is even or odd.
# Function: isEven(int n)

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if isEven(n):
    print("Even")
else:
    print("Odd")
# ____________________________________________________________________________________________________


# 5. Create a function to find the largest of two numbers.
# Function: max(int a, int b)

def max(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Largest:", max(a, b))
# ____________________________________________________________________________________________________


# 6. Create a function to calculate the factorial of a number.
# Function: factorial(int n)

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
# ____________________________________________________________________________________________________


# 7. Create a function to calculate the sum of numbers from 1 to N.
# Function: sum(int n)

def sum(n):
    result = 0

    for i in range(1, n + 1):
        result = result + i

    return result

n = int(input("Enter N: "))
print("Sum:", sum(n))
# ____________________________________________________________________________________________________


# 8. Create a function to count the digits in a number.
# Function: countDigits(int n)

def countDigits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count

n = int(input("Enter a number: "))
print("Number of digits:", countDigits(n))
# ____________________________________________________________________________________________________


# 9. Create a function to check whether a number is a palindrome.
# Function: isPalindrome(int n)

def isPalindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if isPalindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")