# Mini Project - Password Checker

# Check password strength
# 1. Password has at least 8 characters
# 2. Password has at least 1 uppercase letter
# 3. Password has at least 1 number
# 4. Password has at least 1 special character

password = input("Enter password - ")

has_digit = any(x.isdigit() for x in password)  # Checks for a digit
has_upper = any(x.isupper() for x in password)  # Checks for uppercase letter
has_lower = any(x.islower() for x in password)  # Checks for lowercase letter
has_8letter = len(password)  # Checks password length
has_specialLetter = any(not x.isalnum() for x in password)  # Checks for special character

if has_digit and has_upper and has_lower and has_8letter >= 8 and has_specialLetter:
    print("Password is strong")
else:
    if has_digit == False:
        print("Please enter at least one digit")
    if has_upper == False:
        print("Please enter at least one uppercase letter")
    if has_lower == False:
        print("Please enter at least one lowercase letter")
    if has_8letter < 8:
        print("Please enter at least 8 characters")
    if has_specialLetter == False:
        print("Please enter at least one special character")