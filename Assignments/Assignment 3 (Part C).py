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

# Check if a triangle is valid based on 3 sides.
side1 = float(input("Enter value of side 1: "))
side2 = float(input("Enter value of side 2: "))
side3 = float(input("Enter value of side 3: "))
a = side1 + side2
b = side2 + side3
c = side3 + side1
if a > side3 and b > side1 and c > side2:
    print("It is a triangle")
else:
    print("It is mot a triangle")

# Determine salary bonus: 5 years → 10% bonus, 3–5 years → 5%, <3 years → no bonus
year = int(input("Enter your years of experience: "))
if year >= 5:
    print("Your bonus will be 10%")
elif year >= 3:
    print("Your bonus will be 5%")
else:
    print("You will not get any bonus")

# Check login credentials (username & password).
correct_username = "Pranjal Kumar"
correct_password = "python123"
username = input("Enter your username: ")
if correct_username == username:
    password = input("Now, enter your password: ")
    if correct_password == password:
        print("You are logged in.")
    else:
        print("Your entered password is wrong")
else:
    print("Your entered username is wrong")

# Calculate discount:, ≥1000 → 20%, ≥500 → 10%, else → no discount
amount = int(input("Enter your total amount:"))
if amount >= 1000:
    print("You will get 20% discount")
    percent20 = amount / 100 * 20
    print("Your discount amount: ",percent20)
    percent80 = amount - percent20
    print("Your final amount is: ",percent80)

elif amount >= 500:
    print("You will get 10% discount")
    percent10 = amount / 100 * 10
    print("Your discount amount: ",percent10)
    percent90 = amount - percent10
    print("Your final amount is: ",percent90)
else:
    print("You will not get discount")

# Check if a number is divisible by 11 using condition.
number = int(input("Enter a number: "))
if number % 11 == 0: 
    print("The number is divisible by 11")
else:
    print("The number is not divisible by 11")

# Build a menu-driven program using if-elif-else (e.g., ATM system).
print("""-----ATM-----                 
Options:
1. Check Balance
2. Deposit
3. Withdraw
4. EXIT""")                       # Display ATM menu
pin = 1234                        # Store correct ATM PIN
enteredpin = int(input("Enter your Pin: "))   # Take PIN from user
if enteredpin == pin:             # Check if PIN is correct
    option = int(input("Enter your option: "))   # Take menu choice
    if option == 1:               # Option 1 → Check Balance
        print("Your Balance is 10000INR")    # Show balance
    elif option == 2:             # Option 2 → Deposit Money
        amountdeposit = int(input("Enter the amount to deposit: "))   # Input deposit amount
        finalamount = 10000 + amountdeposit    # Add deposit to balance
        print("Now, Your Balance is:", finalamount)   # Display updated balance
    elif option == 3:             # Option 3 → Withdraw Money
        amountwithdraw = int(input("Enter the amount to withdraw: "))   # Input withdraw amount
        if amountwithdraw <= 10000:    # Check sufficient balance
            finalamount = 10000 - amountwithdraw   # Subtract amount
            print("Now, Your Balance is:", finalamount)   # Display updated balance
        else:
            print("Insufficient Balance.")   # Withdrawal not possible
    elif option == 4:             # Option 4 → Exit
        print("Thanks, for visiting")   # Goodbye message
    else:
        print("Invalid Option.")   # Invalid menu choice
else:
    print("Wrong Pin")            # Incorrect PIN