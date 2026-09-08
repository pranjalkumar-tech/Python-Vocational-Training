# Connecting to Database

import sqlite3  # Imports the sqlite3 module

connection = sqlite3.connect("students.db")  # Creates or opens a database
print("Database connected")

connection.close()  # Closes the connection