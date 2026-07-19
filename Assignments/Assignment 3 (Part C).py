# Create a simple calculator using if-else (add, subtract, multiply, divide).
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Enter operator: ")
if operator == "+":
    print("The sum of", num1, "and", num2, "is: ", num1 + num2)
elif operator == "-":
    print("The subtraction of", num2, "from", num1, "is: ", num1 - num2)
elif operator == "*":
    print("The multiplication of", num1, "by", num2, "is: ", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("The division of", num1, "by", num2, "is: ", num1 / num2)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator")

# Find the second largest of three numbers.
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
if num2 > num1 > num3 or num2 < num1 < num3:
    print("The second largest is:", num1)  
elif num1 > num2 > num3 or num1 < num2 < num3:
    print("The second largest is:", num2)
elif num1 > num3 > num2 or num1 < num3 < num2:
    print("The second largest is:", num3)
else:
    print("Second largest does not exist because two or more numbers are equal.")