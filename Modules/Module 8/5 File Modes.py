# File Modes

# "r" is used to read a file
file = open("example.txt", "r")
file.close()

# "w" is used to write to a file
file = open("example.txt", "w")
file.close()

# "a" is used to append data to a file
file = open("example.txt", "a")
file.close()

# "x" is used to create a new file
file = open("newfile.txt", "x")
file.close()