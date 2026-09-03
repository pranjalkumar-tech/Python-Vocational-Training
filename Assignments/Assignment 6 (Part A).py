## 1. Number Classification
# Input 10 numbers. Count how many are:
# - Positive
# - Negative
# - Zero

positive = 0
negative = 0
zero = 0

for num in range(10):
    num = int(input("Enter a number: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero += 1

print("Positive number: ", positive)
print("Negative number: ", negative)
print("Zero: ", zero)
#__________________________________________________________________________________________________________________________________________________________________________


## 2. Sum of Even Numbers
# Input N and calculate the sum of all even numbers from 1 to N.

start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
sum = 0

for num in range(start, end + 1, 1):
    if num % 2 == 0:
        sum += num

print(sum)
#__________________________________________________________________________________________________________________________________________________________________________


## 3. Multiplication Table Generator
# Ask the user for a number and print its multiplication table up to 10. Repeat until the user enters 0 to exit.

num = 1

while num != 0:
    num = int(input("Enter a number: "))

    if num != 0:
        print("The multiplication table of", num, "is:")
        mult = 0
        for mult in range(1, 11, 1):
            print(num, "*", mult, "=", mult * num)

    elif num == 0:
        print("Program Ended")
#__________________________________________________________________________________________________________________________________________________________________________


## 4. Password Validation
# Ask the user to enter a password repeatedly until they enter **"python123"**. Print "Access Granted" when correct.

original_password = "python123"
password = None

while password != original_password:
    password = input("Enter the password: ")

    if password != original_password:
        print("Your entered password is wrong, please try again,")

print("Access Granted")
#__________________________________________________________________________________________________________________________________________________________________________


## 5. Largest of N Numbers
# Input N numbers from the user and print the largest number.

largest = None

while True:
    num = int(input("Enter a number(Use 0 to stop): "))

    if num == 0:
        break
    if largest is None or num > largest:
        largest = num

print("So the largest number is: ", largest)
#__________________________________________________________________________________________________________________________________________________________________________


## 6. Count Digits
# Input a number and print:
# - Total number of digits
# - Sum of digits
# - Largest digit

num = int(input("Enter number: "))
count = 0
sum = 0
largest = 0

while num > 0:
    digit = num % 10
    count += 1
    sum += digit
    if digit > largest:
        largest = digit
    num //= 10

print("Total number of digits: ", count)
print("Sum of digits: ", sum)
print("Largest digit: ", largest)
#__________________________________________________________________________________________________________________________________________________________________________


## 7. Prime Number Checker
#Input a number and determine whether it is prime or not.

num = int(input("Enter a number: "))

if num <= 0 and num <= 1:
    print("It is not a Prime Number")
else:
    prime = True

    for x in range(2,num,1):
        if num % x == 0:
            prime = False
            break

    if prime == True:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number") 
#__________________________________________________________________________________________________________________________________________________________________________


## 8. Print Prime Numbers
# Print all prime numbers between 1 and 100.
