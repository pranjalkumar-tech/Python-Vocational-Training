# 1. Write a Python program to count the total number of vowels (a, e, i, o, u) in a given string.

text = input("Enter a string: ")
count = 0

for char in text:
    if char.lower() in "aeiou":
        count = count + 1

print("Total vowels:", count)
# ____________________________________________________________________________________________________


# 2. Write a Python program to reverse a string without using the built-in reversed() function.

text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)
# ____________________________________________________________________________________________________


# 3. Write a Python program to check whether a given string is a palindrome or not.

text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
# ____________________________________________________________________________________________________


# 4. Write a Python program to count the number of uppercase letters and lowercase letters in a given string.

text = input("Enter a string: ")
uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase = uppercase + 1
    elif char.islower():
        lowercase = lowercase + 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
# ____________________________________________________________________________________________________


# 5. Write a Python program to remove duplicate characters from a string while preserving the original order.

text = input("Enter a string: ")
result = ""

for char in text:
    if char not in result:
        result = result + char

print("String without duplicates:", result)
# ____________________________________________________________________________________________________


# 6. Write a Python program to find the frequency of each character in a string.

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)
# ____________________________________________________________________________________________________


# 7. Write a Python program to replace all spaces in a string with hyphens (-).

text = input("Enter a string: ")

result = text.replace(" ", "-")

print("Result:", result)
# ____________________________________________________________________________________________________


# 8. Write a Python program to find the longest word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
# ____________________________________________________________________________________________________


# 9. Write a Python program to count the total number of words in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Total number of words:", len(words))
# ____________________________________________________________________________________________________


# 10. Write a Python program to check whether two strings are anagrams of each other.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")