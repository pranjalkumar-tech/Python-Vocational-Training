# Creating a Table

import sqlite3

connection = sqlite3.connect("students.db")  # Connects to the database
cursor = connection.cursor()  # Creates a cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")  # Creates the students table

connection.commit()  # Saves the changes
connection.close()  # Closes the connection

print("Table created")
