# Check if a number is positive or negative.
number = int(input("Enter a number: "))
if number > 0:
    print("It is a positive number")
else:
    print("It is a negative number")

# Check if a number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

# Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
     print("The person is eligible for voting")
else:
     print("The person is not eligible for voting")

# Find the largest of two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("the largest number is:", num1)
else:
    print("The largest number is", num2)

# Check if a number is divisible by 5.
number = int(input("Enter a number: "))
if number % 5 == 0: 
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

# Check if a number is divisible by both 3 and 7.
num = int(input("Enter number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Yes")
else:
    print("No")

# Check whether a character is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Check if a number is zero, positive, or negative.
number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")

# Check if a year is a leap year.
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

# Check whether a number is a multiple of 10.
number = int(input("Enter a number: "))
if number % 10 == 0:
    print("The number is a multiple of 10")
else:
    print("The number is not a multiple of 10")