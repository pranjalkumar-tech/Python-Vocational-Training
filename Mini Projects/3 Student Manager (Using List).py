students = []  # Creates an empty list

while True:
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. Insert Student")
    print("3. Remove Student")
    print("4. Remove Last Student")
    print("5. Search Student")
    print("6. Count Student")
    print("7. Sort Students")
    print("8. Reverse Students")
    print("9. Display Students")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)  # Adds student to the list
        print("Student added")

    elif choice == 2:
        name = input("Enter student name: ")
        position = int(input("Enter position: "))
        students.insert(position, name)  # Inserts student at position
        print("Student inserted")

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            students.remove(name)  # Removes the student
            print("Student removed")
        else:
            print("Student not found")

    elif choice == 4:
        if len(students) > 0:
            students.pop()  # Removes the last student
            print("Last student removed")
        else:
            print("List is empty")

    elif choice == 5:
        name = input("Enter student name: ")

        if name in students:
            print("Student found")
        else:
            print("Student not found")

    elif choice == 6:
        name = input("Enter student name: ")
        print("Count:", students.count(name))  # Counts the student

    elif choice == 7:
        students.sort()  # Sorts the list
        print("Students sorted")

    elif choice == 8:
        students.reverse()  # Reverses the list
        print("Students reversed")

    elif choice == 9:
        print("Students:", students)

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")