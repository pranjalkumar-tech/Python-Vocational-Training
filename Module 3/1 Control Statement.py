# Types of Control Statements

# Conditional Statements

# 1. if statement
x = 10
if x > 5:
    print("It is greater than 5")

# 2. if-else statement
y = 3
if y > 5:
    print("It is greater than 5")
else:
    print("It is not greater than 5")

# 3. if-elif-else statement
# Student Grade
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail") 

# 4. Nested if statement
# Voting and Driving License
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")

    if age >= 21:
        print("Can apply for a driving license")
    else:
        print("Cannot apply for a driving license")
else:
    print("Not eligible to vote")

# Looping Statements