# Reading Lines

with open("example.txt", "r") as file:
    line = file.readline()  # Reads one line

    print(line)

with open("example.txt", "r") as file:
    lines = file.readlines()  # Reads all lines

    print(lines)