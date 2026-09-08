# Updating Data

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET age = ? WHERE name = ?",
    (21, "Pranjal")
)  # Updates the age

connection.commit()  # Saves the changes
connection.close()

print("Data updated")