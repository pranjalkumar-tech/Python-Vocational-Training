employees = ("Rahul", "Amit", "Priya", "Neha", "Rohit")  # Creates a tuple

while True:
    print("\n--- Employee Database ---")
    print("1. Display Employees")
    print("2. Count Employee")
    print("3. Search Employee")
    print("4. Display Employee Range")
    print("5. Add Employees")
    print("6. Repeat Employees")
    print("7. Unpack Employees")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Employees:", employees)

    elif choice == 2:
        name = input("Enter employee name: ")
        print("Count:", employees.count(name))  # Counts employee name

    elif choice == 3:
        name = input("Enter employee name: ")

        if name in employees:
            print("Employee found")
            print("Position:", employees.index(name))  # Finds position
        else:
            print("Employee not found")

    elif choice == 4:
        start = int(input("Enter start position: "))
        end = int(input("Enter end position: "))
        print("Employees:", employees[start:end])  # Slices the tuple

    elif choice == 5:
        new_employee = input("Enter employee name: ")
        employees = employees + (new_employee,)  # Adds employee using concatenation
        print("Employee added")

    elif choice == 6:
        times = int(input("Enter number of repetitions: "))
        print(employees * times)  # Repeats the tuple

    elif choice == 7:
        if len(employees) == 5:
            employee1, employee2, employee3, employee4, employee5 = employees
            print(employee1)
            print(employee2)
            print(employee3)
            print(employee4)
            print(employee5)
        else:
            print("Unpacking requires exactly 5 employees")

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")