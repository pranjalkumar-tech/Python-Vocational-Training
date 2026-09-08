# Inserting Data

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Pranjal", 20, "Python")
)  # Inserts a student
 
connection.commit()  # Saves the changes
connection.close()

print("Data inserted")
