# Reading Data

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")  # Selects all students
students = cursor.fetchall()  # Gets all records

for student in students:
    print(student)

connection.close()