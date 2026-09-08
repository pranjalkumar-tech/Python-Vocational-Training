students = {}  # Creates an empty dictionary

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Display Student Names")
    print("6. Display Marks")
    print("7. Display Records")
    print("8. Remove Last Record")
    print("9. Copy Records")
    print("10. Clear Records")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks  # Adds student record
        print("Student added")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students.update({name: marks})  # Updates student marks
            print("Record updated")
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter student name: ")
        marks = students.get(name)  # Gets student marks

        if marks is not None:
            print("Student:", name)
            print("Marks:", marks)
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter student name: ")

        if name in students:
            students.pop(name)  # Removes student record
            print("Student removed")
        else:
            print("Student not found")

    elif choice == 5:
        print("Student Names:", students.keys())  # Displays keys

    elif choice == 6:
        print("Marks:", students.values())  # Displays values

    elif choice == 7:
        print("Student Records:", students.items())  # Displays records

    elif choice == 8:
        if len(students) > 0:
            record = students.popitem()  # Removes last record
            print("Removed:", record)
        else:
            print("Dictionary is empty")

    elif choice == 9:
        student_copy = students.copy()  # Creates a copy
        print("Copied Records:", student_copy)

    elif choice == 10:
        students.clear()  # Removes all records
        print("Records cleared")

    elif choice == 11:
        print("Program ended")
        break

    else:
        print("Invalid choice")