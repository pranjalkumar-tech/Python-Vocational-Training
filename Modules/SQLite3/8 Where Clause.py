# WHERE Clause

import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM students WHERE age > ?",
    (18,)
)  # Selects students older than 18

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()