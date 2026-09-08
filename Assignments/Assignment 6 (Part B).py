# 11. ATM Menu
# Display the following menu repeatedly:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Update the balance after each transaction and stop only when the user selects Exit.

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")
#__________________________________________________________________________________________________________________________________________________________________________


# 12. Login System
# Allow only 3 login attempts.
# If the username and password are correct, print "Login Successful".
# Otherwise, lock the account after 3 failed attempts.

correct_username = "admin"
correct_password = "1234"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break

    else:
        attempts = attempts + 1
        print("Incorrect username or password")

if attempts == 3:
    print("Account Locked")
#__________________________________________________________________________________________________________________________________________________________________________


# 14. Number Pyramid
# Print:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()
#__________________________________________________________________________________________________________________________________________________________________________


# 15. Skip Multiples of 5
# Print numbers from 1 to 100, but skip all multiples of 5 using continue.

for number in range(1, 101):
    if number % 5 == 0:
        continue

    print(number)
#__________________________________________________________________________________________________________________________________________________________________________


# 16. Stop at First Negative Number
# Keep accepting numbers from the user.
# If a negative number is entered, stop the loop using break.
# Finally, print the sum of all positive numbers entered.

total = 0

while True:
    number = float(input("Enter a number: "))

    if number < 0:
        break

    total = total + number

print("Sum of positive numbers:", total)
#__________________________________________________________________________________________________________________________________________________________________________


# 17. Armstrong Numbers
# Print all Armstrong numbers between 1 and 1000.

for number in range(1, 1001):
    temp = number
    digits = len(str(number))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == number:
        print(number)
#__________________________________________________________________________________________________________________________________________________________________________


# 18. Fibonacci Series
# Input N and print the first N terms of the Fibonacci series.
# Also count how many terms are even.

n = int(input("Enter N: "))

first = 0
second = 1
even_count = 0

for i in range(n):
    print(first, end=" ")

    if first % 2 == 0:
        even_count = even_count + 1

    next_number = first + second
    first = second
    second = next_number

print()
print("Even terms:", even_count)
#__________________________________________________________________________________________________________________________________________________________________________


# 19. Mini Calculator
# Create a menu-driven calculator with the following operations:
# Addition
# Subtraction
# Multiplication
# Division
# Exit
# Repeat until the user chooses Exit.

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator closed")
        break

    if choice >= 1 and choice <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)

        elif choice == 2:
            print("Result:", a - b)

        elif choice == 3:
            print("Result:", a * b)

        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")

    else:
        print("Invalid choice")
#__________________________________________________________________________________________________________________________________________________________________________


# 20. Student Management Program
# Create a menu-driven program with the following options:
# 1. Add Student Marks
# 2. Display All Marks
# 3. Find Highest Mark
# 4. Find Lowest Mark
# 5. Calculate Average
# 6. Exit
# Use loops and if-else statements to manage the program.

marks = []

while True:
    print("\n1. Add Student Marks")
    print("2. Display All Marks")
    print("3. Find Highest Mark")
    print("4. Find Lowest Mark")
    print("5. Calculate Average")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mark = float(input("Enter student mark: "))
        marks.append(mark)
        print("Marks added")

    elif choice == 2:
        print("All Marks:", marks)

    elif choice == 3:
        if len(marks) > 0:
            print("Highest Mark:", max(marks))
        else:
            print("No marks available")

    elif choice == 4:
        if len(marks) > 0:
            print("Lowest Mark:", min(marks))
        else:
            print("No marks available")

    elif choice == 5:
        if len(marks) > 0:
            average = sum(marks) / len(marks)
            print("Average:", average)
        else:
            print("No marks available")

    elif choice == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")