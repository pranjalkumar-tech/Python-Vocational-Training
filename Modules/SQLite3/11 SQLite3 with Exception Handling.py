# SQLite3 with Exception Handling

import sqlite3

try:
    connection = sqlite3.connect("students.db")  # Connects to the database
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")  # Reads the data

    for student in cursor.fetchall():
        print(student)

    connection.close()

except sqlite3.Error:
    print("Database error occurred.")