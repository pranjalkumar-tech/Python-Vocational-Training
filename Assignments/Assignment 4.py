# 1 se 10 tak numbers print karo
num = 1
while num <= 10:
    print(num)
    num = num + 1

# 1 se 10 tak even numbers print karo
num = 2
while num <= 10:
    print(num)
    num += 2

# 1 se 10 tak odd numbers print karo
num = 1
while num <= 10:
    print(num)
    num += 2

# 1 se 10 tak numbers ka sum nikalna
num = 1
sum = 0
while num <= 10:
    sum += num
    print(sum)
    num += 1

# 5 ka table print karo (5 x 1 = 5 …)
num = 1
while num <= 10:
    print("5 *", num, "=", num*5)
    num += 1

# 1 se 10 tak numbers reverse order mein print karo
num = 10
while num >= 1:
    print(num)
    num -= 1

# 1 se 20 tak numbers mein se sirf multiples of 3 print karo
num = 1
while num <= 20:
    if num % 3 == 0:
        print(num)
    num += 1

# 1 se 5 tak numbers ka square print karo
num = 1
while num <= 5:
    print(num*num)
    num += 1

# Jab tak user 0 na dale tab tak input lete raho
number = 1
while number != 0:
    number = int(input("Enter a number: "))
    if number != 0:
        print("Your number is: ", number)
print("Program Ended")

# Ek number ka factorial nikalna (e.g., 5! = 120)
num = int(input("Enter a number: "))  # Input value
originalnum = num      # Save original value
factorial = 1  
while num >= 1: 
    factorial *= num
    num -= 1
print("Factorial of", originalnum, "is:", factorial)

# 1 se 50 tak numbers mein se sirf divisible by 5 print karo
num = int(input("Enter a number: "))
originalnum = num
while num <= 50:
    if num % originalnum == 0:
        print(num)
    num += 1