# 1 se 10 tak numbers print karo
for num in range(1, 11, 1):
    print(num)

# 1 se 10 tak even numbers print karo
for num in range(2, 11, 2):
    print(num)

# 1 se 10 tak odd numbers print karo
for num in range(1, 9, 2):
    print(num)

# 1 se 10 tak numbers ka sum nikalna
sum = 0
for num in range(1, 11, 1):
    sum += num
print(sum)

# 5 ka table print karo (5 x 1 = 5 …)
table = 0
for table in range(1, 11, 1):
    print("5 *", table, "=", table * 5)
    table += 1

# 1 se 10 tak numbers reverse order mein print karo
for num in range(10, 0, -1):
    print(num)

# 1 se 20 tak numbers mein se sirf multiples of 3 print karo
for num in range(3, 21, 3):
    print(num)

# 1 se 5 tak numbers ka square print karo
for num in range(1, 6, 1):
    print(num * num)

# Ek number ka factorial nikalna (e.g., 5! = 120)
entered_num = int(input("Enter a number: "))
factorial = 1
for num in range(1, entered_num + 1):
    factorial *= num
print("Factorial of", num, "is:", factorial)

# 1 se 50 tak numbers mein se sirf divisible by 5 print karo
num = int(input("Enter a number: "))
for number in range(num, 51, num):
    print(number)