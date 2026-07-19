# Find the largest of three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
if num1> num2 and num1 > num3:
    print("The largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)

# Check if a number is a 2-digit number or not.
number = int(input("Enter a number: "))
if 10 <= number <= 99:
    print("The number is a 2-digit number")
else:
    print("The number is not a 2-digit number")

# Assign grade based on marks: ≥90 → A, ≥75 → B, ≥50 → C, else → Fail
marks = int(input("Enter the marks: "))
if marks >= 90:
     print("Grade is A")
elif marks >= 75:
     print("Grade is B")
elif marks >= 50:
     print("Grade is C")
else:
     print("Fail")

# Check if a character is uppercase, lowercase, digit, or special character.
char = input("Enter a character: ")
if char.isupper():
    print("The character is uppercase.")
elif char.islower():
     print("The character is lowercase.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")

# Check if a number is within a specific range (e.g., 10 to 50).
num = int(input("Enter a number: "))
if 10<num<50:
    print("The number is in the range")
else:
    print("The number is not in the range")

# 6. Calculate electricity bill based on units: 0–100 → ₹5/unit, 101–200 → ₹7/unit, above 200 → ₹10/unit
unit = int(input("Enter the number of units: "))
if 0<= unit <= 100:
    bill = unit * 5
    print("The bill is", bill)
elif 101 <= unit <= 200:
    bill = unit * 7
    print("The bill is:", bill)
elif 200 < unit:    
    bill = unit * 10
    print("The bill is:", bill)

# Check if a number is divisible by 2 or 3 but not both.
num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 3 != 0:
        print("The number is divisible 2 but not with 3")
    else:
        print("No, The number is divisible with both 2 and 3")    
elif num % 3 == 0:
    if num % 2 != 0:
        print("The number is divisible 3 but not with 2")
    else:
        print("No, The number is divisible with both 2 and 3")  # Already know num is not divisible by 2     
else:
    print("The number is divisible by 2 but not by 3")   

# Determine if a person is a child[less than 14], teenager[14y to 21y], or adult[21+] based on age.
age = int(input("Enter your age: "))
if age < 14:
    print("You are a child")
elif 14 <+ age < 21:
    print("You are a teenegar")
else:
    print("You are a adult")