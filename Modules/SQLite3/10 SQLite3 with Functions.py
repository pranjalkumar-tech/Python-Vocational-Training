# SQLite3 with Functions

import sqlite3

def add_student(name, age, course):  # Adds a student to the database
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    connection.commit()
    connection.close()

add_student("Rahul", 21, "Python")
print("Student added")