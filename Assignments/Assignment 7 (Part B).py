# 11. Write a Python program to capitalize the first letter of every word in a sentence without using the title() method.

sentence = input("Enter a sentence: ")
words = sentence.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print("Result:", " ".join(result))
# ____________________________________________________________________________________________________


# 12. Write a Python program to find the first non-repeated character in a string.

text = input("Enter a string: ")
found = False

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        found = True
        break

if found == False:
    print("No non-repeated character found")
# ____________________________________________________________________________________________________


# 13. Write a Python program to compress a string by replacing consecutive repeated characters with their counts.
# Example: aaabbcccc → a3b2c4

text = input("Enter a string: ")
result = ""
count = 1

for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count = count + 1
    else:
        result = result + text[i] + str(count)
        count = 1

print("Compressed string:", result)
# ____________________________________________________________________________________________________


# 14. Write a Python program to count the number of alphabets, digits, and special characters in a string.

text = input("Enter a string: ")
alphabets = 0
digits = 0
special = 0

for char in text:
    if char.isalpha():
        alphabets = alphabets + 1
    elif char.isdigit():
        digits = digits + 1
    else:
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special)
# ____________________________________________________________________________________________________


# 15. Write a Python program to remove all vowels from a given string.
# Write a Python program to print all characters present at even indexes and odd indexes separately.

text = input("Enter a string: ")

result = ""

for char in text:
    if char.lower() not in "aeiou":
        result = result + char

print("String without vowels:", result)

even = ""
odd = ""

for i in range(len(text)):
    if i % 2 == 0:
        even = even + text[i]
    else:
        odd = odd + text[i]

print("Characters at even indexes:", even)
print("Characters at odd indexes:", odd)
# ____________________________________________________________________________________________________


# 16. Write a Python program to check whether one string is a rotation of another string.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) == len(text2) and text2 in text1 + text1:
    print("String is a rotation")
else:
    print("String is not a rotation")
# ____________________________________________________________________________________________________


# 17. Write a Python program to count the number of occurrences of a given substring in a string.

text = input("Enter a string: ")
substring = input("Enter substring: ")

count = text.count(substring)

print("Number of occurrences:", count)
# ____________________________________________________________________________________________________


# 18. Write a Python program to mask all the middle characters of a string with *, keeping only the first and last characters visible.
# Example: Programming → P**********g

text = input("Enter a string: ")

if len(text) <= 2:
    print(text)
else:
    result = text[0] + "*" * (len(text) - 2) + text[-1]
    print("Masked string:", result)
# ____________________________________________________________________________________________________


# 19. Write a Python program to validate a password using the following conditions:
# Password must contain at least 8 characters.
# It must contain at least one uppercase letter.
# It must contain at least one lowercase letter.
# It must contain at least one digit.
# It must contain at least one special character (@, #, $, %, ^, &, *).

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "@#$%^&*":
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password is valid")
else:
    print("Password is invalid")

    if len(password) < 8:
        print("Password must contain at least 8 characters")
    if has_upper == False:
        print("Password must contain at least one uppercase letter")
    if has_lower == False:
        print("Password must contain at least one lowercase letter")
    if has_digit == False:
        print("Password must contain at least one digit")
    if has_special == False:
        print("Password must contain at least one special character")