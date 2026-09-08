visitors = set()  # Creates an empty set

while True:
    print("\n--- Visitor Management System ---")
    print("1. Add Visitor")
    print("2. Add Multiple Visitors")
    print("3. Remove Visitor")
    print("4. Discard Visitor")
    print("5. Remove Random Visitor")
    print("6. Copy Visitors")
    print("7. Clear Visitors")
    print("8. Display Visitors")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter visitor name: ")
        visitors.add(name)  # Adds visitor to the set
        print("Visitor added")

    elif choice == 2:
        names = input("Enter visitor names separated by comma: ")
        names = names.split(",")
        visitors.update(names)  # Adds multiple visitors
        print("Visitors added")

    elif choice == 3:
        name = input("Enter visitor name: ")

        if name in visitors:
            visitors.remove(name)  # Removes visitor
            print("Visitor removed")
        else:
            print("Visitor not found")

    elif choice == 4:
        name = input("Enter visitor name: ")
        visitors.discard(name)  # Removes visitor if present
        print("Visitor discarded")

    elif choice == 5:
        if len(visitors) > 0:
            visitor = visitors.pop()  # Removes a random visitor
            print("Removed:", visitor)
        else:
            print("Set is empty")

    elif choice == 6:
        visitor_copy = visitors.copy()  # Creates a copy
        print("Copied Set:", visitor_copy)

    elif choice == 7:
        visitors.clear()  # Removes all visitors
        print("Visitors cleared")

    elif choice == 8:
        print("Visitors:", visitors)

    elif choice == 9:
        print("Program ended")
        break

    else:
        print("Invalid choice")