# Reading a File

file = open("example.txt", "r")  # Opens the file in read mode
content = file.read()  # Reads the complete file
print(content)

file.close()  # Closes the file