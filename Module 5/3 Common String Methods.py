# Common String Methods

name = "python"
print(name.upper())  # Convert to uppercase

name = "PYTHON"
print(name.lower())  # Convert to lowercase

name = "python"
print(name.capitalize())  # Capitalize first letter

name = "python core training"
print(name.title())  # Capitalizes the first letter of every word

name = "python"
print(len(name))  # Print length

text = "I love Java"
print(text.replace("Java", "Python"))  # Replace Java with Python

text = "Python"
print(text.find("t"))  # Find index of 't'

text = "banana"
print(text.count("a"))  # # Count the letter 'a'

text = "   Python   "
print(text.strip())  # Remove extra spaces

text = "I love Python"
print(text.split())  # Split into words

text = ["I", "love", "Python"]
print(" ".join(text))  # Join the words with spaces