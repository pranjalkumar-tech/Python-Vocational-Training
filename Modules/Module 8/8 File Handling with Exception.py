# File Handling with Exception

try:
    with open("example.txt", "r") as file:
        content = file.read()  # Reads the file

        print(content)

except FileNotFoundError:
    print("File not found.")