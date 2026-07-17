# Personal Info --- name,age,city
name = "Pranjal Kumar"
age = 20
city = "Raipur"
print("Personal Information:-")
print("- Name:", name)
print("- Age:", age)
print("- City:", city)

# User Input (Name and age ) - welcome name and age.
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print("Welcome", Name, "and", Age)

#Program -- two number addition, subtraction, multiplication, division, modulus
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
print("Addition of these two number is", num1+num2)
print("Subtraction of these two number is", num1-num2)
print("Multiplication of these two number is", num1*num2)
print("Division of these two number is", num1/num2)
print("Modulus of these two number is", num1%num2)

# Simple Interest Formula - SI = (P * R * T) / 100
P = float(input("Enter Principal Amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))
SI = (P * R * T) / 100
print("Simple Interest is", SI)

# Swap Two Variables: a = 10, b = 20
# 1st Method: Using 3rd variable
a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)
temp = a # temp = 10
a = b    # a = 20
b = temp # b = 10
print("After swapping:")
print("a =", a)
print("b =", b)
 
# 2nd Method: Using without 3rd variable
a = 10
b = 20
print("Before swapping: a =", a, "b =", b)
a, b = b, a 
print("After swapping: a =", a, "b =", b)

# Area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length*width
print("Area of Rectangle:", area)

# Square of Number
number = float(input("Enter a number to find its square: "))
square = number**2
print("Square of", number, "is", square)  

# Cube of Number
number = float(input("Enter a number to find its cube: "))  
cube = number**3
print("Cube of", number, "is", cube)      

# Total Marks & Percentage of students (5 subjects max marks - 100)
english = float(input("Enter marks obtained in English: "))
maths = float(input("Enter marks obtained in Maths: "))
science = float(input("Enter marks obtained in Science: "))
social_studies = float(input("Enter marks obtained in Social Studies: "))
hindi = float(input("Enter marks obtained in Hindi: "))
total_marks = english + maths + science + social_studies + hindi
percentage = (total_marks / 500) * 100
print("Total Marks:", total_marks)
print("Percentage:", percentage)

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "Celsius is equal to", fahrenheit, "Fahrenheit")

# Area of Circle
radius = float(input("Enter radius of circle:"))
area = 3.14 * radius*radius
print("Area of Circle:", area)