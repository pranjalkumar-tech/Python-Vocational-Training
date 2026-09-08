# With Statement
# with automatically closes the file after use.

with open("example.txt", "r") as file:
    content = file.read()  # Reads the file

    print(content)