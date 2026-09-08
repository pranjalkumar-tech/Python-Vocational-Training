FILE_NAME = "students.txt"  # Stores the file name

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(roll + "," + name + "," + age + "," + course + "\n")

    print("Student Added Successfully")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n------ Student Records ------")

            found = False

            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    print("Roll   :", data[0])
                    print("Name   :", data[1])
                    print("Age    :", data[2])
                    print("Course :", data[3])
                    print("-----------------------------")
                    found = True

            if found == False:
                print("No Records Found")

    except FileNotFoundError:
        print("No Records Found")

def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4 and data[0] == roll:
                    print("\nStudent Found")
                    print("Roll   :", data[0])
                    print("Name   :", data[1])
                    print("Age    :", data[2])
                    print("Course :", data[3])

                    found = True
                    break

        if found == False:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")

def update_student():
    roll = input("Enter Roll Number to Update: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for line in lines:
                data = line.strip().split(",")

                if len(data) == 4 and data[0] == roll:
                    print("Enter New Details")

                    name = input("Name: ")
                    age = input("Age: ")
                    course = input("Course: ")

                    file.write(roll + "," + name + "," + age + "," + course + "\n")

                    found = True

                else:
                    file.write(line)

        if found:
            print("Record Updated Successfully")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for line in lines:
                data = line.strip().split(",")

                if len(data) == 4 and data[0] != roll:
                    file.write(line)
                else:
                    if len(data) == 4 and data[0] == roll:
                        found = True

        if found:
            print("Record Deleted Successfully")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")

while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")