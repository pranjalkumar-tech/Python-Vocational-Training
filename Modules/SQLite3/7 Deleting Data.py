# Deleting Data

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Pranjal",)
)  # Deletes the student

connection.commit()  # Saves the changes
connection.close()

print("Data deleted")